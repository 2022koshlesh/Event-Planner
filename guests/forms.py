from django import forms

from .models import RSVP, Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["first_name", "last_name", "email", "phone_number"]


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ["status", "number_of_guests", "notes"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 3}),
        }
