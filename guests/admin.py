from django.contrib import admin

from .models import RSVP, Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "event"]
    list_filter = ["event"]
    search_fields = ["first_name", "last_name", "email"]


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ["guest", "status", "number_of_guests", "response_date"]
    list_filter = ["status"]
    search_fields = ["guest__first_name", "guest__last_name"]
