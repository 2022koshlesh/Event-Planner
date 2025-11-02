from django import forms

from .models import EventVendor, Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            "name",
            "category",
            "contact_person",
            "email",
            "phone_number",
            "notes",
        ]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 3}),
        }


class EventVendorForm(forms.ModelForm):
    class Meta:
        model = EventVendor
        fields = ["vendor", "service_description", "contract_amount", "status"]
        widgets = {
            "service_description": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        event = kwargs.pop("event", None)
        super().__init__(*args, **kwargs)
        self.event = event

        if event:
            # Exclude vendors already assigned to this event
            already_assigned = EventVendor.objects.filter(event=event).values_list("vendor_id", flat=True)
            self.fields["vendor"].queryset = Vendor.objects.exclude(id__in=already_assigned)

    def clean(self):
        cleaned_data = super().clean()
        vendor = cleaned_data.get("vendor")

        if vendor and self.event:
            # Check if this vendor is already assigned to the event
            if EventVendor.objects.filter(event=self.event, vendor=vendor).exists():
                raise forms.ValidationError(f"{vendor.name} is already assigned to this event.")

        return cleaned_data
