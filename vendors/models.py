from django.db import models

from events.models import Event


class Vendor(models.Model):
    CATEGORY_CHOICES = [
        ("catering", "Catering"),
        ("photography", "Photography"),
        ("decoration", "Decoration"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class EventVendor(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_vendors")
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="event_vendors")
    service_description = models.TextField()
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        unique_together = ["event", "vendor"]

    def __str__(self):
        return f"{self.vendor.name} - {self.event.title}"
