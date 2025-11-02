from django import forms
from django.contrib.auth import get_user_model

from .models import RSVP, Invitation

User = get_user_model()


class InvitationForm(forms.ModelForm):
    """Form for sending invitations to users"""

    invitee = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        help_text="Select a user to invite to this event",
    )

    class Meta:
        model = Invitation
        fields = ["invitee", "notes"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 3, "placeholder": "Optional message to the invitee"}),
        }

    def __init__(self, *args, **kwargs):
        event = kwargs.pop("event", None)
        super().__init__(*args, **kwargs)
        
        if event:
            # Exclude users already invited or the event organizer
            already_invited = Invitation.objects.filter(event=event).values_list("invitee_id", flat=True)
            self.fields["invitee"].queryset = User.objects.exclude(
                id__in=list(already_invited) + [event.created_by.id]
            )


class RSVPForm(forms.ModelForm):
    """Form for updating RSVP details"""

    class Meta:
        model = RSVP
        fields = ["status", "number_of_guests", "notes"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 3}),
        }
