from django.urls import path

from .views import (
    GuestDeleteView,
    GuestListView,
    InvitationCreateView,
    InvitationDeleteView,
    InvitationListView,
    InvitationRespondView,
    MyInvitationsView,
    RSVPUpdateView,
)

app_name = "guests"

urlpatterns = [
    # Invitation management (for event organizers)
    path("event/<int:event_pk>/invitations/", InvitationListView.as_view(), name="invitation_list"),
    path("event/<int:event_pk>/invitations/send/", InvitationCreateView.as_view(), name="invitation_create"),
    path("invitations/<int:pk>/cancel/", InvitationDeleteView.as_view(), name="invitation_delete"),
    # My invitations (for invitees)
    path("my-invitations/", MyInvitationsView.as_view(), name="my_invitations"),
    path("invitations/<int:pk>/<str:action>/", InvitationRespondView.as_view(), name="invitation_respond"),
    # Guest management (confirmed guests)
    path("event/<int:event_pk>/guests/", GuestListView.as_view(), name="guest_list"),
    path("guests/<int:pk>/remove/", GuestDeleteView.as_view(), name="guest_delete"),
    # RSVP management
    path("rsvp/<int:pk>/edit/", RSVPUpdateView.as_view(), name="rsvp_edit"),
]
