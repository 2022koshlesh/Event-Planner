from django import template

from guests.models import Invitation

register = template.Library()


@register.simple_tag
def get_pending_invitation_count(user):
    """Get the count of pending invitations for a user"""
    if user.is_authenticated:
        return Invitation.objects.filter(invitee=user, status="pending").count()
    return 0

