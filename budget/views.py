from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from events.models import Event

from .forms import BudgetItemForm
from .models import BudgetItem


class BudgetListView(LoginRequiredMixin, ListView):
    model = BudgetItem
    template_name = "budget/budget_list.html"
    context_object_name = "budget_items"

    def get_queryset(self):
        self.event = get_object_or_404(Event, pk=self.kwargs["event_pk"], created_by=self.request.user)
        return BudgetItem.objects.filter(event=self.event)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = self.event
        context["total_estimated"] = self.get_queryset().aggregate(Sum("estimated_cost"))["estimated_cost__sum"] or 0
        context["total_actual"] = self.get_queryset().aggregate(Sum("actual_cost"))["actual_cost__sum"] or 0
        return context


class BudgetItemCreateView(LoginRequiredMixin, CreateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = "budget/budgetitem_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        return context

    def form_valid(self, form):
        form.instance.event = get_object_or_404(Event, pk=self.kwargs["event_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("budget:budget_list", kwargs={"event_pk": self.kwargs["event_pk"]})


class BudgetItemUpdateView(LoginRequiredMixin, UpdateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = "budget/budgetitem_form.html"

    def get_success_url(self):
        return reverse_lazy("budget:budget_list", kwargs={"event_pk": self.object.event.pk})


class BudgetItemDeleteView(LoginRequiredMixin, DeleteView):
    model = BudgetItem
    template_name = "budget/budgetitem_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("budget:budget_list", kwargs={"event_pk": self.object.event.pk})
