from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()


@register.filter
def timesince_short(value):
    """
    Returns a human-readable time difference.
    Examples: "2 hours ago", "3 days ago", "just now"
    """
    if not value:
        return ""
    
    now = timezone.now()
    diff = now - value
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return "just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif seconds < 604800:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"
    elif seconds < 2592000:
        weeks = int(seconds / 604800)
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"
    elif seconds < 31536000:
        months = int(seconds / 2592000)
        return f"{months} month{'s' if months != 1 else ''} ago"
    else:
        years = int(seconds / 31536000)
        return f"{years} year{'s' if years != 1 else ''} ago"


@register.filter
def mask_phone(phone_number):
    """
    Masks a phone number, showing only the last 2 digits.
    Example: "9876543221" becomes "********21"
    """
    if not phone_number:
        return ""
    
    phone_str = str(phone_number)
    
    # Show only last 2 digits
    if len(phone_str) > 2:
        masked = '*' * (len(phone_str) - 2) + phone_str[-2:]
    elif len(phone_str) == 2:
        masked = '**'
    else:
        masked = '*' * len(phone_str)
    
    return masked
