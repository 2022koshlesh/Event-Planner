from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import Event

from .models import Guest, Invitation, RSVP

User = get_user_model()


class InvitationModelTestCase(TestCase):
    """Test cases for Invitation model"""

    def setUp(self):
        """Set up test data"""
        self.organizer = User.objects.create_user(
            username="organizer", email="organizer@example.com", password="testpass123"
        )
        self.invitee = User.objects.create_user(
            username="invitee", email="invitee@example.com", password="testpass123"
        )
        
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            event_type="wedding",
            status="planning",
            start_date=timezone.now() + timezone.timedelta(days=30),
            end_date=timezone.now() + timezone.timedelta(days=30, hours=5),
            venue="Test Venue",
            location="Test Location",
            max_capacity=100,
            created_by=self.organizer,
        )

    def test_invitation_creation(self):
        """Test invitation creation with default values"""
        invitation = Invitation.objects.create(event=self.event, invitee=self.invitee)
        self.assertEqual(invitation.status, "pending")
        self.assertEqual(invitation.event, self.event)
        self.assertEqual(invitation.invitee, self.invitee)
        self.assertIsNotNone(invitation.invited_at)
        self.assertIsNone(invitation.responded_at)

    def test_invitation_str_representation(self):
        """Test invitation string representation"""
        invitation = Invitation.objects.create(event=self.event, invitee=self.invitee)
        expected = f"{self.invitee.get_full_name() or self.invitee.username} - {self.event.title} (pending)"
        self.assertEqual(str(invitation), expected)

    def test_invitation_unique_together(self):
        """Test that a user can't be invited twice to the same event"""
        Invitation.objects.create(event=self.event, invitee=self.invitee)
        with self.assertRaises(Exception):
            Invitation.objects.create(event=self.event, invitee=self.invitee)


class GuestModelTestCase(TestCase):
    """Test cases for updated Guest model"""

    def setUp(self):
        """Set up test data"""
        self.organizer = User.objects.create_user(
            username="organizer", email="organizer@example.com", password="testpass123"
        )
        self.guest_user = User.objects.create_user(
            username="guestuser", email="guest@example.com", password="testpass123"
        )
        
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            event_type="wedding",
            status="planning",
            start_date=timezone.now() + timezone.timedelta(days=30),
            end_date=timezone.now() + timezone.timedelta(days=30, hours=5),
            venue="Test Venue",
            location="Test Location",
            max_capacity=100,
            created_by=self.organizer,
        )

    def test_guest_creation(self):
        """Test guest creation"""
        guest = Guest.objects.create(event=self.event, user=self.guest_user)
        self.assertEqual(guest.event, self.event)
        self.assertEqual(guest.user, self.guest_user)
        self.assertIsNotNone(guest.added_at)

    def test_guest_str_representation(self):
        """Test guest string representation"""
        guest = Guest.objects.create(event=self.event, user=self.guest_user)
        expected = f"{self.guest_user.get_full_name() or self.guest_user.username} - {self.event.title}"
        self.assertEqual(str(guest), expected)

    def test_guest_unique_together(self):
        """Test that a user can't be a guest twice for the same event"""
        Guest.objects.create(event=self.event, user=self.guest_user)
        with self.assertRaises(Exception):
            Guest.objects.create(event=self.event, user=self.guest_user)


class InvitationViewTestCase(TestCase):
    """Test cases for Invitation views"""

    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.organizer = User.objects.create_user(
            username="organizer", email="organizer@example.com", password="testpass123"
        )
        self.invitee = User.objects.create_user(
            username="invitee", email="invitee@example.com", password="testpass123", first_name="John", last_name="Doe"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", email="other@example.com", password="testpass123"
        )
        
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            event_type="wedding",
            status="planning",
            start_date=timezone.now() + timezone.timedelta(days=30),
            end_date=timezone.now() + timezone.timedelta(days=30, hours=5),
            venue="Test Venue",
            location="Test Location",
            max_capacity=100,
            created_by=self.organizer,
        )

    def test_invitation_list_requires_login(self):
        """Test that invitation list requires login"""
        url = reverse("guests:invitation_list", kwargs={"event_pk": self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_invitation_list_success(self):
        """Test invitation list view displays invitations"""
        invitation = Invitation.objects.create(event=self.event, invitee=self.invitee)
        
        # Verify the invitation was created with pending status
        self.assertEqual(invitation.status, "pending")
        self.assertEqual(Invitation.objects.filter(event=self.event, status="pending").count(), 1)
        
        self.client.login(username="organizer", password="testpass123")
        url = reverse("guests:invitation_list", kwargs={"event_pk": self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        # Verify the invitations are in the list
        self.assertIn(invitation, response.context["invitations"])

    def test_invitation_create_requires_login(self):
        """Test that invitation create requires login"""
        url = reverse("guests:invitation_create", kwargs={"event_pk": self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_invitation_create_get(self):
        """Test invitation create view GET request"""
        self.client.login(username="organizer", password="testpass123")
        url = reverse("guests:invitation_create", kwargs={"event_pk": self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("event", response.context)

    def test_invitation_create_post_success(self):
        """Test invitation create view POST request creates invitation"""
        self.client.login(username="organizer", password="testpass123")
        url = reverse("guests:invitation_create", kwargs={"event_pk": self.event.pk})
        data = {
            "invitee": self.invitee.pk,
            "notes": "Please join us!",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        
        # Check invitation was created
        invitation = Invitation.objects.get(event=self.event, invitee=self.invitee)
        self.assertEqual(invitation.notes, "Please join us!")
        self.assertEqual(invitation.status, "pending")

    def test_invitation_respond_accept(self):
        """Test accepting an invitation"""
        invitation = Invitation.objects.create(event=self.event, invitee=self.invitee)
        self.client.login(username="invitee", password="testpass123")
        
        url = reverse("guests:invitation_respond", kwargs={"pk": invitation.pk, "action": "accept"})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        
        # Check invitation was accepted
        invitation.refresh_from_db()
        self.assertEqual(invitation.status, "accepted")
        self.assertIsNotNone(invitation.responded_at)
        
        # Check guest was created
        self.assertTrue(Guest.objects.filter(event=self.event, user=self.invitee).exists())
        
        # Check RSVP was created
        guest = Guest.objects.get(event=self.event, user=self.invitee)
        self.assertTrue(RSVP.objects.filter(guest=guest).exists())

    def test_invitation_respond_decline(self):
        """Test declining an invitation"""
        invitation = Invitation.objects.create(event=self.event, invitee=self.invitee)
        self.client.login(username="invitee", password="testpass123")
        
        url = reverse("guests:invitation_respond", kwargs={"pk": invitation.pk, "action": "decline"})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        
        # Check invitation was declined
        invitation.refresh_from_db()
        self.assertEqual(invitation.status, "declined")
        self.assertIsNotNone(invitation.responded_at)
        
        # Check guest was not created
        self.assertFalse(Guest.objects.filter(event=self.event, user=self.invitee).exists())

    def test_my_invitations_view(self):
        """Test my invitations view shows user's invitations"""
        pending_invitation = Invitation.objects.create(event=self.event, invitee=self.invitee)
        
        # Create another event and accepted invitation
        event2 = Event.objects.create(
            title="Another Event",
            description="Test",
            event_type="party",
            status="planning",
            start_date=timezone.now() + timezone.timedelta(days=60),
            end_date=timezone.now() + timezone.timedelta(days=60, hours=3),
            venue="Another Venue",
            location="Another Location",
            max_capacity=50,
            created_by=self.other_user,
        )
        accepted_invitation = Invitation.objects.create(
            event=event2, invitee=self.invitee, status="accepted", responded_at=timezone.now()
        )
        
        self.client.login(username="invitee", password="testpass123")
        url = reverse("guests:my_invitations")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(pending_invitation, response.context["pending_invitations"])
        self.assertIn(accepted_invitation, response.context["responded_invitations"])

    def test_invitation_delete_requires_organizer(self):
        """Test that only the event organizer can cancel invitations"""
        invitation = Invitation.objects.create(event=self.event, invitee=self.invitee)
        
        # Try as another user
        self.client.login(username="otheruser", password="testpass123")
        url = reverse("guests:invitation_delete", kwargs={"pk": invitation.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
        # Try as organizer
        self.client.login(username="organizer", password="testpass123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class GuestViewTestCase(TestCase):
    """Test cases for Guest views"""

    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.organizer = User.objects.create_user(
            username="organizer", email="organizer@example.com", password="testpass123"
        )
        self.guest_user = User.objects.create_user(
            username="guestuser", email="guest@example.com", password="testpass123", first_name="Jane", last_name="Smith"
        )
        
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            event_type="wedding",
            status="planning",
            start_date=timezone.now() + timezone.timedelta(days=30),
            end_date=timezone.now() + timezone.timedelta(days=30, hours=5),
            venue="Test Venue",
            location="Test Location",
            max_capacity=100,
            created_by=self.organizer,
        )
        
        self.guest = Guest.objects.create(event=self.event, user=self.guest_user)
        self.rsvp = RSVP.objects.create(guest=self.guest)

    def test_guest_list_requires_login(self):
        """Test that guest list requires login"""
        url = reverse("guests:guest_list", kwargs={"event_pk": self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_guest_list_success(self):
        """Test guest list view displays guests"""
        self.client.login(username="organizer", password="testpass123")
        url = reverse("guests:guest_list", kwargs={"event_pk": self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Smith")

    def test_guest_delete_success(self):
        """Test guest delete removes guest"""
        self.client.login(username="organizer", password="testpass123")
        guest_pk = self.guest.pk
        url = reverse("guests:guest_delete", kwargs={"pk": guest_pk})
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Guest.objects.filter(pk=guest_pk).exists())


class RSVPViewTestCase(TestCase):
    """Test cases for RSVP views"""

    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.organizer = User.objects.create_user(
            username="organizer", email="organizer@example.com", password="testpass123"
        )
        self.guest_user = User.objects.create_user(
            username="guestuser", email="guest@example.com", password="testpass123"
        )
        
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            event_type="wedding",
            status="planning",
            start_date=timezone.now() + timezone.timedelta(days=30),
            end_date=timezone.now() + timezone.timedelta(days=30, hours=5),
            venue="Test Venue",
            location="Test Location",
            max_capacity=100,
            created_by=self.organizer,
        )
        
        self.guest = Guest.objects.create(event=self.event, user=self.guest_user)
        self.rsvp = RSVP.objects.create(guest=self.guest)

    def test_rsvp_update_requires_login(self):
        """Test that RSVP update requires login"""
        url = reverse("guests:rsvp_edit", kwargs={"pk": self.rsvp.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_rsvp_update_success(self):
        """Test RSVP update view updates RSVP"""
        self.client.login(username="organizer", password="testpass123")
        url = reverse("guests:rsvp_edit", kwargs={"pk": self.rsvp.pk})
        data = {
            "status": "accepted",
            "number_of_guests": 2,
            "notes": "Looking forward!",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        
        self.rsvp.refresh_from_db()
        self.assertEqual(self.rsvp.status, "accepted")
        self.assertEqual(self.rsvp.number_of_guests, 2)


class InvitationTemplateTagTestCase(TestCase):
    """Test cases for invitation template tags"""

    def setUp(self):
        """Set up test data"""
        self.organizer = User.objects.create_user(
            username="organizer", email="organizer@example.com", password="testpass123"
        )
        self.invitee = User.objects.create_user(
            username="invitee", email="invitee@example.com", password="testpass123"
        )
        
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            event_type="wedding",
            status="planning",
            start_date=timezone.now() + timezone.timedelta(days=30),
            end_date=timezone.now() + timezone.timedelta(days=30, hours=5),
            venue="Test Venue",
            location="Test Location",
            max_capacity=100,
            created_by=self.organizer,
        )

    def test_get_pending_invitation_count(self):
        """Test getting pending invitation count"""
        from guests.templatetags.invitation_tags import get_pending_invitation_count
        
        # Create pending invitations
        Invitation.objects.create(event=self.event, invitee=self.invitee, status="pending")
        Invitation.objects.create(
            event=self.event,
            invitee=User.objects.create_user(username="user2", email="user2@example.com", password="pass"),
            status="accepted",
        )
        
        count = get_pending_invitation_count(self.invitee)
        self.assertEqual(count, 1)
