from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "event_type", "status", "start_date", "created_by"]
    list_filter = ["event_type", "status", "start_date"]
    search_fields = ["title", "description", "venue"]
    date_hierarchy = "start_date"
