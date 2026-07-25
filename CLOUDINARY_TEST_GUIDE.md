# Cloudinary Testing Guide

## Quick Test (2 Minutes)

### Step 1: Set Environment Variables

Create `.env` file in project root:

```env
# Copy from .env.example and fill in

CLOUDINARY_CLOUD_NAME=dk0bhqeuf
CLOUDINARY_API_KEY=your-actual-api-key
CLOUDINARY_API_SECRET=your-actual-api-secret

# Other required vars
DJANGO_ENV=development
DEBUG=True
SECRET_KEY=django-insecure-test-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 2: Start Server

```bash
python manage.py runserver
```

### Step 3: Test Profile Picture Upload

1. Go to http://127.0.0.1:8000/accounts/profile/
2. Click "Edit Profile"
3. Upload a profile picture
4. Save

**Expected Result:**
- Image uploads successfully
- Image displays on profile page
- Image URL starts with: `https://res.cloudinary.com/dk0bhqeuf/...`

### Step 4: Test Post Image Upload

1. Go to http://127.0.0.1:8000/posts/create/
2. Fill in post details
3. Upload an image
4. Submit

**Expected Result:**
- Post created successfully
- Image displays in post card
- Image URL is Cloudinary URL

### Step 5: Verify in Database

```bash
python manage.py shell
```

```python
# Check profile avatar URL
from accounts.models import Profile
profile = Profile.objects.last()
print(profile.avatar.url if profile.avatar else "No avatar")
# Should print: https://res.cloudinary.com/dk0bhqeuf/image/upload/...

# Check post image URL
from posts.models import Post
post = Post.objects.last()
print(post.image.url if post.image else "No image")
# Should print: https://res.cloudinary.com/dk0bhqeuf/image/upload/...
```

### Step 6: Verify in Cloudinary Dashboard

1. Go to https://cloudinary.com/console
2. Log in
3. Click "Media Library"
4. You should see:
   - `profiles/` folder with profile pictures
   - `posts/` folder with post images

---

## ✅ Success Criteria

- [ ] Environment variables set correctly
- [ ] Server starts without errors
- [ ] Profile picture uploads to Cloudinary
- [ ] Profile picture displays correctly
- [ ] Post image uploads to Cloudinary
- [ ] Post image displays correctly
- [ ] Image URLs are Cloudinary URLs (not local `/media/` URLs)
- [ ] Images visible in Cloudinary dashboard
- [ ] Static files (CSS) still load correctly

---

## 🐛 Common Issues

### Issue: Images Upload to Local media/ Folder

**Cause:** Environment variables not loaded

**Fix:**
```bash
# Verify .env file exists
ls .env

# Verify variables are set
python manage.py shell
>>> import os
>>> print(os.environ.get('CLOUDINARY_CLOUD_NAME'))
# Should print: dk0bhqeuf (not None)
```

### Issue: "Cloudinary credentials not found" Error

**Fix:**
```bash
# Check settings
python manage.py shell
>>> from django.conf import settings
>>> print(settings.CLOUDINARY_STORAGE)
# Should print: {'CLOUD_NAME': 'dk0bhqeuf', 'API_KEY': '...', 'API_SECRET': '...'}

# If empty, check .env file and restart server
```

### Issue: Static Files Not Loading

**Fix:**
```bash
# Verify STORAGES configuration
python manage.py shell
>>> from django.conf import settings
>>> print(settings.STORAGES['staticfiles'])
# Should print: {'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'}

# Run collectstatic
python manage.py collectstatic --noinput
```

---

## 📝 Quick Commands

```bash
# Verify Cloudinary package installed
python -c "import cloudinary; import cloudinary_storage; print('✅ OK')"

# Check Django configuration
python manage.py check

# Test environment variables
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('CLOUDINARY_CLOUD_NAME'))"

# Run migrations (if needed)
python manage.py migrate

# Create test superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

---

## 🎯 What Should Work

### ✅ Working:
- Static files (CSS, JS) via WhiteNoise
- Media files (images) via Cloudinary
- Profile picture upload
- Post image upload
- Image display in templates
- Admin interface uploads
- All existing functionality

### ❌ Should NOT Work (Intentionally):
- Local media file serving (removed, uses Cloudinary)
- Direct access to `/media/` URLs (uses Cloudinary CDN)

---

## 🚀 Ready for Production

Once local testing passes:

1. Set environment variables on deployment platform:
   ```
   CLOUDINARY_CLOUD_NAME=dk0bhqeuf
   CLOUDINARY_API_KEY=your-key
   CLOUDINARY_API_SECRET=your-secret
   ```

2. Deploy as usual - no additional steps needed

3. Images will automatically upload to Cloudinary

4. Images accessible worldwide via CDN

---

**Status:** Ready to test  
**Time Required:** 2-5 minutes  
**Prerequisites:** Cloudinary credentials
