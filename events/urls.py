from django.urls import path

from .views import (
    DashboardView,
    EventCreateView,
    EventDeleteView,
    EventDetailView,
    EventListView,
    EventUpdateView,
)

app_name = "events"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("events/", EventListView.as_view(), name="event_list"),
    path("events/create/", EventCreateView.as_view(), name="event_create"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("events/<int:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("events/<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
]
