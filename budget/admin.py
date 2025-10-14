from django.contrib import admin

from .models import BudgetItem


@admin.register(BudgetItem)
class BudgetItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "event",
        "estimated_cost",
        "actual_cost",
        "status",
    ]
    list_filter = ["category", "status"]
    search_fields = ["name", "event__title"]
