from django.contrib import admin

from .models import EventVendor, Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "contact_person", "email", "phone_number"]
    list_filter = ["category"]
    search_fields = ["name", "contact_person", "email"]


@admin.register(EventVendor)
class EventVendorAdmin(admin.ModelAdmin):
    list_display = ["vendor", "event", "contract_amount", "status"]
    list_filter = ["status"]
    search_fields = ["vendor__name", "event__title"]
