from django.conf import settings
from django.db import models

from events.models import Event


class Invitation(models.Model):
    """Model to track event invitations sent to users"""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="invitations")
    invitee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="event_invitations"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    invited_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, help_text="Message from the event organizer")

    class Meta:
        ordering = ["-invited_at"]
        unique_together = ["event", "invitee"]

    def __str__(self):
        return f"{self.invitee.get_full_name() or self.invitee.username} - {self.event.title} ({self.status})"


class Guest(models.Model):
    """Model for confirmed event guests (users who accepted invitations)"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="guests")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="guest_events")
    invitation = models.OneToOneField(
        Invitation, on_delete=models.SET_NULL, null=True, blank=True, related_name="guest"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["user__last_name", "user__first_name"]
        unique_together = ["event", "user"]

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.event.title}"


class RSVP(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
    ]

    guest = models.OneToOneField(Guest, on_delete=models.CASCADE, related_name="rsvp")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    number_of_guests = models.PositiveIntegerField(default=1)
    response_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.guest} - {self.status}"
