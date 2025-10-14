from django.urls import path
from .views import GuestListView, GuestCreateView, GuestUpdateView, GuestDeleteView, RSVPUpdateView

app_name = "guests"

urlpatterns = [
    path("event/<int:event_pk>/guests/", GuestListView.as_view(), name="guest_list"),
    path("event/<int:event_pk>/guests/create/", GuestCreateView.as_view(), name="guest_create"),
    path("guests/<int:pk>/edit/", GuestUpdateView.as_view(), name="guest_edit"),
    path("guests/<int:pk>/delete/", GuestDeleteView.as_view(), name="guest_delete"),
    path("rsvp/<int:pk>/edit/", RSVPUpdateView.as_view(), name="rsvp_edit"),
]

