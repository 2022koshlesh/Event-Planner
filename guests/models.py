from django.db import models
from events.models import Event


class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="guests")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["last_name", "first_name"]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
