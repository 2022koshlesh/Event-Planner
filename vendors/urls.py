from django.urls import path

from .views import (
    EventVendorCreateView,
    EventVendorDeleteView,
    EventVendorListView,
    EventVendorUpdateView,
    VendorCreateView,
    VendorDeleteView,
    VendorListView,
    VendorUpdateView,
)

app_name = "vendors"

urlpatterns = [
    path("vendors/", VendorListView.as_view(), name="vendor_list"),
    path("vendors/create/", VendorCreateView.as_view(), name="vendor_create"),
    path("vendors/<int:pk>/edit/", VendorUpdateView.as_view(), name="vendor_edit"),
    path("vendors/<int:pk>/delete/", VendorDeleteView.as_view(), name="vendor_delete"),
    path(
        "event/<int:event_pk>/vendors/",
        EventVendorListView.as_view(),
        name="eventvendor_list",
    ),
    path(
        "event/<int:event_pk>/vendors/assign/",
        EventVendorCreateView.as_view(),
        name="eventvendor_create",
    ),
    path(
        "eventvendors/<int:pk>/edit/",
        EventVendorUpdateView.as_view(),
        name="eventvendor_edit",
    ),
    path(
        "eventvendors/<int:pk>/delete/",
        EventVendorDeleteView.as_view(),
        name="eventvendor_delete",
    ),
]
