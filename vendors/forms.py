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
