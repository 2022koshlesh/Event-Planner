from django import forms

from vendors.models import EventVendor

from .models import BudgetItem


class BudgetItemForm(forms.ModelForm):
    class Meta:
        model = BudgetItem
        fields = [
            "category",
            "name",
            "vendor",
            "estimated_cost",
            "actual_cost",
            "status",
            "payment_date",
        ]
        widgets = {
            "payment_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        event = kwargs.pop("event", None)
        super().__init__(*args, **kwargs)

        if event:
            # Filter vendors to only show those assigned to this event
            self.fields["vendor"].queryset = EventVendor.objects.filter(event=event).select_related("vendor")
            self.fields["vendor"].label_from_instance = (
                lambda obj: f"{obj.vendor.name} ({obj.vendor.get_category_display()}) - ${obj.contract_amount}"
            )
            # Add widget attributes for JavaScript filtering
            self.fields["vendor"].widget.attrs.update({"class": "form-select vendor-select"})
