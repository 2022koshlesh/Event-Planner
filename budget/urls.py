from django.urls import path

from .views import (
    BudgetItemCreateView,
    BudgetItemDeleteView,
    BudgetItemUpdateView,
    BudgetListView,
)

app_name = "budget"

urlpatterns = [
    path("event/<int:event_pk>/budget/", BudgetListView.as_view(), name="budget_list"),
    path(
        "event/<int:event_pk>/budget/create/",
        BudgetItemCreateView.as_view(),
        name="budgetitem_create",
    ),
    path("budget/<int:pk>/edit/", BudgetItemUpdateView.as_view(), name="budgetitem_edit"),
    path(
        "budget/<int:pk>/delete/",
        BudgetItemDeleteView.as_view(),
        name="budgetitem_delete",
    ),
]
