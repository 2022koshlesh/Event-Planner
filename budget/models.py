from django.db import models

from events.models import Event
from vendors.models import EventVendor


class BudgetItem(models.Model):
    CATEGORY_CHOICES = [
        ("venue", "Venue"),
        ("catering", "Catering"),
        ("decoration", "Decoration"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("paid", "Paid"),
        ("pending", "Pending"),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="budget_items")
    vendor = models.ForeignKey(
        EventVendor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="budget_items",
        help_text="Optional: Link this budget item to a vendor",
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    actual_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planned")
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"
