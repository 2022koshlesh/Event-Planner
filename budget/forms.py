from django import forms

from .models import BudgetItem


class BudgetItemForm(forms.ModelForm):
    class Meta:
        model = BudgetItem
        fields = [
            "category",
            "name",
            "estimated_cost",
            "actual_cost",
            "status",
            "payment_date",
        ]
        widgets = {
            "payment_date": forms.DateInput(attrs={"type": "date"}),
        }
