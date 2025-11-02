from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

from events.models import Event

from .forms import InvitationForm, RSVPForm
from .models import RSVP, Guest, Invitation


class InvitationListView(LoginRequiredMixin, ListView):
    """View to list all invitations for an event"""

    model = Invitation
    template_name = "guests/invitation_list.html"
    context_object_name = "invitations"

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs["event_pk"], created_by=self.request.user)
        return Invitation.objects.filter(event=self.event).select_related("invitee")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = self.event
        context["pending_count"] = self.get_queryset().filter(status="pending").count()
        context["accepted_count"] = self.get_queryset().filter(status="accepted").count()
        context["declined_count"] = self.get_queryset().filter(status="declined").count()
        return context


class InvitationCreateView(LoginRequiredMixin, CreateView):
    """View to send invitations to users"""

    model = Invitation
    form_class = InvitationForm
    template_name = "guests/invitation_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["event"] = get_object_or_404(Event, pk=self.kwargs["event_pk"], created_by=self.request.user)
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        return context

    def form_valid(self, form):
        form.instance.event = get_object_or_404(Event, pk=self.kwargs["event_pk"], created_by=self.request.user)
        response = super().form_valid(form)
        messages.success(
            self.request, f"Invitation sent to {self.object.invitee.get_full_name() or self.object.invitee.username}!"
        )
        return response

    def get_success_url(self):
        return reverse_lazy("guests:invitation_list", kwargs={"event_pk": self.kwargs["event_pk"]})


class InvitationDeleteView(LoginRequiredMixin, DeleteView):
    """View to cancel/delete an invitation"""

    model = Invitation
    template_name = "guests/invitation_confirm_delete.html"

    def get_queryset(self):
        return Invitation.objects.filter(event__created_by=self.request.user)

    def get_success_url(self):
        messages.success(self.request, "Invitation cancelled successfully.")
        return reverse_lazy("guests:invitation_list", kwargs={"event_pk": self.object.event.pk})


class MyInvitationsView(LoginRequiredMixin, ListView):
    """View for users to see their received invitations"""

    model = Invitation
    template_name = "guests/my_invitations.html"
    context_object_name = "invitations"

    def get_queryset(self):
        return Invitation.objects.filter(invitee=self.request.user).select_related("event", "event__created_by")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pending_invitations"] = self.get_queryset().filter(status="pending")
        context["responded_invitations"] = self.get_queryset().exclude(status="pending")
        return context


class InvitationRespondView(LoginRequiredMixin, View):
    """View to accept or decline an invitation"""

    def post(self, request, pk, action):
        invitation = get_object_or_404(Invitation, pk=pk, invitee=request.user, status="pending")

        if action == "accept":
            invitation.status = "accepted"
            invitation.responded_at = timezone.now()
            invitation.save()

            # Create Guest record
            guest, created = Guest.objects.get_or_create(
                event=invitation.event, user=request.user, defaults={"invitation": invitation}
            )

            # Create RSVP record
            RSVP.objects.get_or_create(guest=guest)

            messages.success(request, f"You have accepted the invitation to {invitation.event.title}!")

        elif action == "decline":
            invitation.status = "declined"
            invitation.responded_at = timezone.now()
            invitation.save()
            messages.info(request, f"You have declined the invitation to {invitation.event.title}.")

        return redirect("guests:my_invitations")


class GuestListView(LoginRequiredMixin, ListView):
    """View to list all confirmed guests for an event"""

    model = Guest
    template_name = "guests/guest_list.html"
    context_object_name = "guests"

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs["event_pk"], created_by=self.request.user)
        return Guest.objects.filter(event=self.event).select_related("user", "rsvp")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = self.event
        return context


class GuestDeleteView(LoginRequiredMixin, DeleteView):
    """View to remove a guest from an event"""

    model = Guest
    template_name = "guests/guest_confirm_delete.html"

    def get_queryset(self):
        return Guest.objects.filter(event__created_by=self.request.user)

    def get_success_url(self):
        messages.success(self.request, "Guest removed from event.")
        return reverse_lazy("guests:guest_list", kwargs={"event_pk": self.object.event.pk})


class RSVPUpdateView(LoginRequiredMixin, UpdateView):
    """View to update RSVP details"""

    model = RSVP
    form_class = RSVPForm
    template_name = "guests/rsvp_form.html"

    def get_queryset(self):
        return RSVP.objects.filter(guest__event__created_by=self.request.user)

    def get_success_url(self):
        return reverse_lazy("guests:guest_list", kwargs={"event_pk": self.object.guest.event.pk})
