# Post Expiry System - Implementation Summary

## ✅ Implementation Complete

Automatic post expiry system implemented for CampusHub with management command and visual indicators.

## Requirements vs Implementation

| Requirement | Status | Implementation |
|-------------|--------|----------------|
| 30-day expiry | ✅ | Posts expire 30 days after creation |
| Hide from Browse | ✅ | Filtered by `is_active=True` |
| Hide from Search | ✅ | Filtered by `is_active=True` |
| Hide from Home | ✅ | Filtered by `is_active=True` |
| Management command | ✅ | `expire_posts` command created |
| Expiry display | ✅ | "Expires in X days" badge shown |

## What Was Built

### 1. Model Methods (posts/models.py)
```python
# Added to Post model
def get_expiry_date(self):
    return self.created_at + timedelta(days=30)

def is_expired(self):
    return timezone.now() > self.get_expiry_date()

def days_until_expiry(self):
    time_diff = self.get_expiry_date() - timezone.now()
    return max(0, time_diff.days)

def get_expiry_display(self):
    days = self.days_until_expiry()
    if days == 0:
        return "Expires today"
    elif days == 1:
        return "Expires in 1 day"
    else:
        return f"Expires in {days} days"
```

### 2. Management Command
**File:** `posts/management/commands/expire_posts.py`

**Usage:**
```bash
# Expire posts
python manage.py expire_posts

# Preview (dry-run)
python manage.py expire_posts --dry-run

# Help
python manage.py expire_posts --help
```

**What it does:**
- Finds active posts older than 30 days
- Marks them as `is_active=False`
- Shows summary with count and dates
- Color-coded output
- Dry-run mode for testing

### 3. Template Updates
Added expiry badges to:
- ✅ `templates/posts/post_list.html` (Browse Posts)
- ✅ `templates/posts/my_posts.html` (My Posts)
- ✅ `templates/posts/post_detail.html` (Post Detail)
- ✅ `templates/core/home.html` (Home Page)

**Display:**
```
🕒 Expires in 15 days  (Gray - Normal)
🕒 Expires in 5 days   (Orange - Warning)
🕒 Expires in 2 days   (Red - Urgent)
🕒 Expires today       (Red - Urgent)
```

## Color Coding

| Days Remaining | Color | Purpose |
|----------------|-------|---------|
| 0-3 days | 🔴 Red | Urgent |
| 4-7 days | 🟠 Orange | Warning |
| 8-30 days | ⚪ Gray | Normal |

## Files Modified/Created

### Modified (5 files)
```
✏️ posts/models.py
   - Added timezone import
   - Added 4 expiry methods

✏️ templates/posts/post_list.html
   - Added expiry badge to post cards

✏️ templates/posts/my_posts.html
   - Added expiry badge to post cards

✏️ templates/posts/post_detail.html
   - Added expiry info in meta section

✏️ templates/core/home.html
   - Added expiry badge to post cards
```

### Created (4 files)
```
✨ posts/management/__init__.py
   - Management module init

✨ posts/management/commands/__init__.py
   - Commands module init

✨ posts/management/commands/expire_posts.py
   - Django management command (120 lines)

✨ POST_EXPIRY_COMPLETE.md
   - Detailed documentation

✨ POST_EXPIRY_SUMMARY.md
   - This file
```

## How It Works

### Timeline Example
```
Day 0:  Post created
        Expiry: 30 days from now
        Display: "Expires in 30 days"
        Status: Active ✓

Day 15: Display: "Expires in 15 days" (Gray)
        Status: Active ✓

Day 25: Display: "Expires in 5 days" (Orange)
        Status: Active ✓

Day 29: Display: "Expires in 1 day" (Red)
        Status: Active ✓

Day 30: Display: "Expires today" (Red)
        Status: Active ✓

Day 31: Command runs: expire_posts
        Status: Inactive ✗
        Visibility: Hidden everywhere
```

## Command Output Examples

### No Expiry Needed
```bash
$ python manage.py expire_posts
No posts to expire.
```

### Posts Expired
```bash
$ python manage.py expire_posts
Successfully expired 8 post(s).
Summary:
  - Posts expired: 8
  - Cutoff date: 2026-06-23 10:30:15
  - Current time: 2026-07-23 10:30:15
```

### Dry-Run Mode
```bash
$ python manage.py expire_posts --dry-run
DRY RUN: Would expire 3 post(s):
  - [42] Looking for roommate (Created 35 days ago)
  - [38] iPhone for sale (Created 32 days ago)
  - [35] Flat available (Created 31 days ago)
```

## Scheduling Options

### Linux/Mac Cron
```bash
# Run daily at 2 AM
0 2 * * * cd /path/to/project && python manage.py expire_posts
```

### Windows Task Scheduler
```batch
REM expire_posts.bat
cd D:\Startup\campushubadypu
python manage.py expire_posts

REM Schedule in Task Scheduler to run daily at 2 AM
```

### Manual Run
```bash
# Anytime you want
python manage.py expire_posts
```

## View Filtering

All views already filter by `is_active=True`:

```python
# Browse Posts
Post.objects.filter(is_active=True)

# Home Page
Post.objects.filter(is_active=True)[:8]

# My Posts
Post.objects.filter(user=request.user, is_active=True)

# Result: Expired posts automatically hidden
```

## Visual Examples

### Post List Card
```
┌─────────────────────────────┐
│ [Image or Gradient]         │
│                             │
│ [Roommate Badge]            │
│ Looking for Roommate        │
│ 📍 Pune · 2d ago            │
│ ₹5000 · 2d ago              │
│ 🕒 Expires in 15 days       │ ← New!
└─────────────────────────────┘
```

### Post Detail Page
```
Posted: July 8, 2026 (15d ago)
🕒 Expires in 15 days          ← New!
```

### My Posts Card
```
View | Edit | Delete
🕒 Expires in 5 days          ← Orange warning!
```

## Edge Cases Handled

✅ **Post exactly 30 days old**
   → Shows "Expires today", active until command runs

✅ **Command runs multiple times**
   → Idempotent, safe to run repeatedly

✅ **User's own expired posts**
   → Hidden from "My Posts", cannot edit

✅ **Manually deleted posts**
   → Already inactive, command ignores

✅ **No posts to expire**
   → Clean message, no errors

## Testing Status

```bash
✅ python manage.py check
   System check identified no issues

✅ python manage.py expire_posts --help
   Shows usage information

✅ python manage.py expire_posts --dry-run
   Preview mode works

✅ python manage.py expire_posts
   Command executes successfully

✅ python -m py_compile posts/models.py
   No syntax errors

✅ Template rendering tested
   Badges display correctly
```

## Performance Impact

### Database
- No new fields added
- Uses existing `created_at` field
- Simple date calculation
- Minimal overhead

### Views
- Already filtering `is_active=True`
- No additional queries
- No performance degradation

### Command
- Single batch update query
- Runs outside user requests
- Scheduled during low traffic

## Benefits

### Users
- ✅ See only fresh, relevant content
- ✅ Know when posts expire
- ✅ Urgency indicators
- ✅ Better experience

### System
- ✅ Automated cleanup
- ✅ No manual intervention
- ✅ Reduced clutter
- ✅ Better data quality

### Admins
- ✅ Schedulable command
- ✅ Dry-run testing
- ✅ Clear audit trail
- ✅ Easy monitoring

## Data Retention

**Important:** Expired posts are NOT deleted!

- `is_active` set to `False`
- Data remains in database
- Can be analyzed or restored
- Can be purged manually if needed

## Future Enhancements (Not Implemented)

- Renewal option (extend by 30 days)
- Email notifications before expiry
- Different expiry per category
- Admin dashboard for expired posts
- Auto-delete after 90 days inactive

## Quick Reference

### Check Expiry
```python
post = Post.objects.get(pk=1)
print(post.days_until_expiry())     # e.g., 15
print(post.get_expiry_display())    # "Expires in 15 days"
print(post.is_expired())            # False
```

### Run Command
```bash
# Preview
python manage.py expire_posts --dry-run

# Execute
python manage.py expire_posts
```

### Template Usage
```django
<!-- Show expiry -->
{{ post.get_expiry_display }}

<!-- Days remaining -->
{{ post.days_until_expiry }}

<!-- Conditional styling -->
{% if post.days_until_expiry <= 3 %}
  <span class="urgent">Expiring soon!</span>
{% endif %}
```

## Configuration

### Change Expiry Period
Edit `posts/models.py`:
```python
def get_expiry_date(self):
    return self.created_at + timedelta(days=30)  # Change 30 here
```

### Change Color Thresholds
Edit templates:
```django
{% if post.days_until_expiry <= 3 %}  <!-- Change thresholds -->
  bg-red-100 text-red-700
{% elif post.days_until_expiry <= 7 %}
  bg-orange-100 text-orange-700
{% endif %}
```

## 🎉 Status: COMPLETE

### All Requirements Met
- ✅ 30-day automatic expiry
- ✅ Expired posts hidden everywhere
- ✅ Management command created
- ✅ Expiry display implemented
- ✅ Color-coded urgency
- ✅ Comprehensive documentation

### Production Ready
- ✅ No errors or warnings
- ✅ Tested and verified
- ✅ Schedulable
- ✅ Dry-run mode
- ✅ Well documented

---

**Implementation Date:** July 23, 2026  
**Status:** COMPLETE ✅  
**Ready for deployment**

### Next Steps for Admins
1. Schedule `expire_posts` command to run daily
2. Monitor command execution
3. Review expired posts periodically
4. Consider data retention policy
