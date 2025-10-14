from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from events.models import Event

from .forms import GuestForm, RSVPForm
from .models import RSVP, Guest


class GuestListView(LoginRequiredMixin, ListView):
    model = Guest
    template_name = "guests/guest_list.html"
    context_object_name = "guests"

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs["event_pk"], created_by=self.request.user)
        return Guest.objects.filter(event=self.event)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = self.event
        return context


class GuestCreateView(LoginRequiredMixin, CreateView):
    model = Guest
    form_class = GuestForm
    template_name = "guests/guest_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        return context

    def form_valid(self, form):
        form.instance.event = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        response = super().form_valid(form)
        RSVP.objects.create(guest=self.object)
        return response

    def get_success_url(self):
        return reverse_lazy("guests:guest_list", kwargs={"event_pk": self.kwargs["event_pk"]})


class GuestUpdateView(LoginRequiredMixin, UpdateView):
    model = Guest
    form_class = GuestForm
    template_name = "guests/guest_form.html"

    def get_success_url(self):
        return reverse_lazy("guests:guest_list", kwargs={"event_pk": self.object.event.pk})


class GuestDeleteView(LoginRequiredMixin, DeleteView):
    model = Guest
    template_name = "guests/guest_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("guests:guest_list", kwargs={"event_pk": self.object.event.pk})


class RSVPUpdateView(LoginRequiredMixin, UpdateView):
    model = RSVP
    form_class = RSVPForm
    template_name = "guests/rsvp_form.html"

    def get_success_url(self):
        return reverse_lazy("guests:guest_list", kwargs={"event_pk": self.object.guest.event.pk})
