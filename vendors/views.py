from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from events.models import Event
from .models import Vendor, EventVendor
from .forms import VendorForm, EventVendorForm


class VendorListView(LoginRequiredMixin, ListView):
    model = Vendor
    template_name = "vendors/vendor_list.html"
    context_object_name = "vendors"


class VendorCreateView(LoginRequiredMixin, CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendors/vendor_form.html"
    success_url = reverse_lazy("vendors:vendor_list")


class VendorUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendors/vendor_form.html"
    success_url = reverse_lazy("vendors:vendor_list")


class VendorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendor
    template_name = "vendors/vendor_confirm_delete.html"
    success_url = reverse_lazy("vendors:vendor_list")


class EventVendorListView(LoginRequiredMixin, ListView):
    model = EventVendor
    template_name = "vendors/eventvendor_list.html"
    context_object_name = "event_vendors"
    
    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs["event_pk"], created_by=self.request.user)
        return EventVendor.objects.filter(event=self.event)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = self.event
        return context


class EventVendorCreateView(LoginRequiredMixin, CreateView):
    model = EventVendor
    form_class = EventVendorForm
    template_name = "vendors/eventvendor_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        return context
    
    def form_valid(self, form):
        form.instance.event = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("vendors:eventvendor_list", kwargs={"event_pk": self.kwargs["event_pk"]})


class EventVendorUpdateView(LoginRequiredMixin, UpdateView):
    model = EventVendor
    form_class = EventVendorForm
    template_name = "vendors/eventvendor_form.html"
    
    def get_success_url(self):
        return reverse_lazy("vendors:eventvendor_list", kwargs={"event_pk": self.object.event.pk})


class EventVendorDeleteView(LoginRequiredMixin, DeleteView):
    model = EventVendor
    template_name = "vendors/eventvendor_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("vendors:eventvendor_list", kwargs={"event_pk": self.object.event.pk})
