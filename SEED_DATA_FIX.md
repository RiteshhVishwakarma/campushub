# Seed Data Command - Bug Fix

## Issue
The initial implementation attempted to manually create Profile objects, but the `accounts` app has a signal that automatically creates profiles when users are created. This caused an `IntegrityError: UNIQUE constraint failed: accounts_profile.user_id`.

## Root Cause
```python
# accounts/signals.py
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a Profile automatically when a User is created"""
    if created:
        Profile.objects.get_or_create(user=instance)
```

The signal auto-creates profiles, so manually calling `Profile.objects.create()` in the seed command caused duplicate creation attempts.

## Solution
Changed from **creating** profiles to **updating** existing auto-created profiles:

### Before (Caused Error)
```python
# Create user
user = User.objects.create_user(...)

# Create profile (ERROR: Already created by signal!)
Profile.objects.create(
    user=user,
    phone=...,
    bio=...,
    college=...
)
```

### After (Fixed)
```python
# Create user (signal auto-creates profile)
user = User.objects.create_user(...)

# Update the auto-created profile
profile = user.profile
profile.phone = ...
profile.bio = ...
profile.college = ...
profile.save()
```

## Testing

### Command Works
```bash
python manage.py seed_data
# Output: Created 30 users, 100 posts
```

### Clear and Regenerate Works
```bash
python manage.py seed_data --clear
# Output: Deleted 30 seed users, Created 30 users, 100 posts
```

### Data Verification
- ✅ 30 users created with Indian names
- ✅ 100 posts created across all categories:
  - 25 Roommate posts
  - 25 Flat/PG posts
  - 20 Event posts
  - 15 Internship posts
  - 15 Buy & Sell posts
- ✅ All profiles have phone, bio, and college data
- ✅ Posts use realistic Pune locations
- ✅ Appropriate price ranges per category

## Status
✅ **Fixed and Tested**

The seed_data command now works perfectly with the existing signal-based profile creation system.
