from django.contrib import admin

from .models import Guest, Invitation, RSVP


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ["invitee", "event", "status", "invited_at", "responded_at"]
    list_filter = ["status", "invited_at"]
    search_fields = ["invitee__username", "invitee__email", "invitee__first_name", "invitee__last_name", "event__title"]
    readonly_fields = ["invited_at", "responded_at"]
    date_hierarchy = "invited_at"


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ["user", "event", "added_at"]
    list_filter = ["event", "added_at"]
    search_fields = ["user__username", "user__email", "user__first_name", "user__last_name", "event__title"]
    readonly_fields = ["added_at"]
    date_hierarchy = "added_at"


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ["guest", "status", "number_of_guests", "response_date"]
    list_filter = ["status", "response_date"]
    search_fields = ["guest__user__username", "guest__user__first_name", "guest__user__last_name"]
    date_hierarchy = "response_date"
