# CampusHub - Testing Guide

## 🧪 Quick Testing Steps

### Prerequisites
```bash
# Start the server
.\env\Scripts\activate
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## Test Scenario 1: Anonymous User

### ✅ Can Do:
1. **Browse Home Page**
   - Go to http://127.0.0.1:8000/
   - Should see hero section and categories

2. **Browse Posts**
   - Go to http://127.0.0.1:8000/posts/
   - Should see all posts (or empty state)
   - Try category filters

3. **View Post Details**
   - Click on any post
   - Should see full post information
   - Should see "Contact Owner" button with tel: link

### ❌ Cannot Do:
1. **Create Post**
   - Click "Create Post" button
   - Should redirect to login page with `?next=/posts/create/`

2. **Access My Posts**
   - Go to http://127.0.0.1:8000/posts/my-posts/
   - Should redirect to login

---

## Test Scenario 2: Register New User

1. Go to http://127.0.0.1:8000/accounts/register/
2. Fill in:
   - Name: "Test User"
   - Username: "testuser"
   - Email: "test@example.com"
   - Password: "securepass123"
   - Confirm Password: "securepass123"
3. Click "Create Account"
4. Should see success message
5. Should be logged in automatically
6. Profile should be auto-created

---

## Test Scenario 3: Create Post

1. **Login** (if not already)
2. Go to http://127.0.0.1:8000/posts/create/
3. Fill in:
   - Category: "Roommate"
   - Title: "Looking for Roommate Near Campus"
   - Description: "I need a roommate for a 2BHK apartment..."
   - Price: "5000" (optional)
   - Location: "Bangalore, India"
   - Phone: "9876543210"
   - Image: Upload any image (optional)
4. Click "Publish Post"
5. Should see success message
6. Should redirect to post detail page
7. Should see "Edit Post" and "Delete Post" buttons (owner only)

---

## Test Scenario 4: Browse & Filter Posts

1. Go to http://127.0.0.1:8000/posts/
2. Should see the post you created
3. Click on different category filters:
   - "Roommate"
   - "Flat / PG"
   - "Events"
   - etc.
4. Posts should filter accordingly
5. Each card should show:
   - Image or placeholder
   - Category badge
   - Title
   - Location
   - Price (if set)
   - Time (e.g., "2 minutes ago")

---

## Test Scenario 5: View Post Details

1. Click on your post from browse page
2. Should see:
   - Full image
   - Category badge
   - Title
   - Location with icon
   - Price with icon (if set)
   - Posted by your name
   - Posted date
   - Full description
   - "Contact Owner" button
   - "Edit Post" button (since you're owner)
   - "Delete Post" button (since you're owner)

---

## Test Scenario 6: Edit Post

1. On post detail page, click "Edit Post"
2. Form should be pre-filled with existing data
3. Update some fields:
   - Change title
   - Update description
   - Change price
4. Click "Update Post"
5. Should see success message
6. Should redirect back to post detail
7. Changes should be visible

---

## Test Scenario 7: My Posts

1. Click on your avatar (top right)
2. Click "My Posts" from dropdown
3. Should see all your posts
4. Each post card should have:
   - View button
   - Edit button
   - Delete button
5. Try each button

---

## Test Scenario 8: Delete Post

### Option 1: From My Posts
1. Go to "My Posts"
2. Click "Delete" on a post
3. Confirm deletion
4. Should see success message
5. Post should disappear

### Option 2: From Post Detail
1. Go to post detail page
2. Click "Delete Post"
3. Confirm deletion
4. Should redirect to "My Posts"
5. Should see success message

---

## Test Scenario 9: Access Control

### Test 1: Try to Edit Someone Else's Post
1. Create a second user account
2. Try to edit the first user's post
3. Manually go to `/posts/1/edit/`
4. Should get 403 Forbidden error

### Test 2: Try to Delete Someone Else's Post
1. Try to access `/posts/1/delete/`
2. Should get 403 Forbidden error

---

## Test Scenario 10: Category Filtering

1. Create posts in different categories:
   - Create a "Roommate" post
   - Create a "Flat / PG" post
   - Create an "Event" post
   - Create an "Internship" post
   - Create a "Buy & Sell" post

2. Go to browse page
3. Test each filter button
4. Should only show posts from that category

---

## Test Scenario 11: Mobile Responsiveness

1. Open browser DevTools (F12)
2. Toggle device toolbar
3. Test on different screen sizes:
   - Mobile (375px)
   - Tablet (768px)
   - Desktop (1024px+)

4. Check:
   - Navigation works
   - Forms are usable
   - Buttons are large enough
   - Grid layout adjusts (1/2/3 columns)
   - Bottom navigation appears on mobile

---

## Test Scenario 12: Messages

### Success Messages
- Register → "Welcome to CampusHub..."
- Login → "Welcome back..."
- Logout → "You have been logged out..."
- Create Post → "Your post has been created..."
- Update Post → "Your post has been updated..."
- Delete Post → "Your post has been deleted..."

### Check:
- Messages appear at top
- Color-coded (green for success, red for errors)
- Auto-hide after 5 seconds

---

## Test Scenario 13: Relative Time

1. Create a post
2. Check time display:
   - Should say "just now"
3. Wait a few minutes, refresh
4. Should say "X minutes ago"
5. Time format should be human-readable

---

## Test Scenario 14: Image Handling

### With Image
1. Create post with image
2. Image should display on:
   - Browse page (card)
   - Detail page (large)
   - My Posts page (card)

### Without Image
1. Create post without image
2. Placeholder should show:
   - Gradient background
   - First letter of title in white

---

## Test Scenario 15: Contact Feature

1. View any post detail
2. Click "Contact Owner" button
3. Should trigger device's phone dialer (on mobile)
4. Should show phone number: `tel:XXXXXXXXXX`

---

## 🐛 Common Issues to Check

### Issue 1: Images Not Loading
- Check MEDIA_URL in settings
- Check media folder exists
- Check DEBUG = True for development

### Issue 2: Permission Denied
- Check LoginRequiredMixin is working
- Check UserPassesTestMixin test_func

### Issue 3: Template Not Found
- Check template paths
- Check app is in INSTALLED_APPS

### Issue 4: Form Not Saving
- Check CSRF token is present
- Check form.is_valid()
- Check required fields

---

## ✅ Expected Results Summary

| Action | Anonymous | Logged In | Owner |
|--------|-----------|-----------|-------|
| Browse Posts | ✅ | ✅ | ✅ |
| View Details | ✅ | ✅ | ✅ |
| Create Post | ❌ | ✅ | ✅ |
| Edit Post | ❌ | ❌ | ✅ |
| Delete Post | ❌ | ❌ | ✅ |
| My Posts | ❌ | ✅ | ✅ |

---

## 📸 Screenshots to Verify

1. Home page with categories
2. Browse page with posts grid
3. Post detail page with contact button
4. Create post form
5. Edit post form
6. My Posts page
7. Mobile navigation
8. Success messages
9. Category filters
10. Empty state

---

## 🎉 All Tests Pass?

If all scenarios work correctly:
- ✅ Post CRUD is fully functional
- ✅ Access control is working
- ✅ UI is mobile-first and responsive
- ✅ Forms validate properly
- ✅ Messages display correctly
- ✅ Images upload successfully

**Status: Ready for Production!**

---

**Last Updated:** July 23, 2026
