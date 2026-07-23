# CampusHub Project Structure

## Project Overview
CampusHub - Student community platform for discovering roommates, flats, internships, events, and marketplace listings.

---

## Directory Structure

```
campushubadypu/
├── .env.example                          # Environment variables template
├── .gitignore                            # Git ignore rules
├── db.sqlite3                            # SQLite database (development)
├── manage.py                             # Django management script
├── requirements.txt                      # Python dependencies
│
├── campushub/                            # Main project package
│   ├── __init__.py
│   ├── asgi.py                          # ASGI configuration
│   ├── urls.py                          # Root URL configuration
│   ├── wsgi.py                          # WSGI configuration
│   ├── settings.py.backup               # Old settings (backed up)
│   └── settings/                        # ✨ NEW: Settings package
│       ├── __init__.py                  # Auto-loads environment
│       ├── base.py                      # Common settings
│       ├── development.py               # Development settings
│       └── production.py                # Production settings
│
├── core/                                 # Core app (landing, about)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── management/                      # ✨ NEW: Management commands
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── seed_data.py             # ✨ NEW: Seed data command
│   └── migrations/
│
├── accounts/                             # User authentication & profiles
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py                        # Profile model
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── management/
│   │   └── commands/
│   │       └── create_missing_profiles.py
│   └── migrations/
│
├── posts/                                # Posts app (main functionality)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py                        # Post & Report models
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── management/
│   │   └── commands/
│   │       └── expire_posts.py          # Post expiry command
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── post_extras.py               # Custom template tags
│   └── migrations/
│
├── static/                               # Static files
│   ├── css/
│   │   └── style.css                    # Main stylesheet
│   └── js/
│
├── media/                                # User-uploaded files
│   └── profiles/
│       └── [profile photos]
│
├── templates/                            # HTML templates
│   ├── base.html                        # Base template
│   ├── accounts/
│   │   ├── edit_profile.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   └── register.html
│   ├── core/
│   │   ├── home.html                    # Landing page
│   │   └── about.html                   # ✨ NEW: About page
│   ├── posts/
│   │   ├── my_posts.html
│   │   ├── post_create.html
│   │   ├── post_detail.html
│   │   ├── post_edit.html
│   │   └── post_list.html
│   └── components/
│       ├── bottom_nav.html              # Mobile bottom nav
│       ├── mobile_nav.html              # Mobile top nav
│       └── pagination.html              # Pagination component
│
└── Documentation/                        # ✨ NEW: Complete documentation
    ├── ABOUT_MODULE_SUMMARY.md
    ├── ABOUT_PAGE_COMPLETE.md
    ├── AUTHENTICATION_COMPLETE.md
    ├── AUTHENTICATION_SUMMARY.md
    ├── DEPLOYMENT_CHECKLIST.md          # ✨ NEW: Deployment guide
    ├── FINAL_IMPLEMENTATION_SUMMARY.md  # ✨ NEW: Final summary
    ├── LANDING_PAGE_COMPLETE.md
    ├── MODELS_COMPLETE.md
    ├── MVP_COMPLETE_SUMMARY.md
    ├── PAGINATION_COMPLETE.md
    ├── PAGINATION_QUICK_REFERENCE.md
    ├── PAGINATION_SUMMARY.md
    ├── POST_CRUD_COMPLETE.md
    ├── POST_EXPIRY_COMPLETE.md
    ├── POST_EXPIRY_SUMMARY.md
    ├── PRODUCTION_PREPARATION_SUMMARY.md  # ✨ NEW: Production summary
    ├── PRODUCTION_QUICK_REFERENCE.md      # ✨ NEW: Quick reference
    ├── PRODUCTION_READY_COMPLETE.md       # ✨ NEW: Complete guide
    ├── PROFILE_BUG_FIX.md
    ├── PROFILE_CHECKLIST.md
    ├── PROFILE_FEATURES.md
    ├── PROFILE_IMPLEMENTATION_SUMMARY.md
    ├── PROFILE_MODULE_COMPLETE.md
    ├── PROJECT_STATUS.md
    ├── PROJECT_STRUCTURE.md             # ✨ NEW: This file
    ├── PROTECTED_CONTACT_FEATURE.md
    ├── QUICKSTART.md
    ├── README.md
    ├── SEARCH_DISCOVERY_FEATURES.md
    └── UI_POLISH_GUIDE.md
```

---

## Key Features by App

### Core App
- Landing page with hero section
- Category cards (Roommate, Flat/PG, Events, Internship, Buy & Sell)
- About page (founder story)
- ✨ Seed data management command

### Accounts App
- User registration & authentication
- Profile management (photo, bio, phone, college)
- Edit profile functionality
- Profile signal for auto-creation

### Posts App
- CRUD operations for posts
- 5 categories (Roommate, Flat/PG, Event, Internship, Buy & Sell)
- Search & filter functionality
- Pagination (15 posts per page)
- 30-day post expiry system
- Report functionality
- Image upload support

---

## Database Models

### User (Django Built-in)
- username
- email
- password
- first_name
- last_name

### Profile (extends User)
- user (OneToOne)
- phone
- bio (max 120 chars)
- college
- profile_photo
- created_at

### Post
- user (ForeignKey)
- title
- description
- category (ROOMMATE, FLAT_PG, EVENT, INTERNSHIP, BUY_SELL)
- price (optional)
- location
- phone
- image (optional)
- created_at
- updated_at
- is_active (boolean)

### Report
- post (ForeignKey)
- user (ForeignKey)
- reason (SPAM, FAKE, WRONG_CATEGORY, SCAM, OTHER)
- created_at

---

## URL Structure

```
/                              # Landing page
/about/                        # About page
/accounts/register/            # User registration
/accounts/login/               # User login
/accounts/logout/              # User logout
/accounts/profile/<username>/  # User profile
/accounts/profile/edit/        # Edit profile
/posts/                        # Browse all posts
/posts/create/                 # Create new post
/posts/<id>/                   # Post detail
/posts/<id>/edit/              # Edit post
/posts/<id>/delete/            # Delete post
/posts/my-posts/               # User's posts
/admin/                        # Django admin
```

---

## Management Commands

### Core App
```bash
python manage.py seed_data          # Generate seed data
python manage.py seed_data --clear  # Clear and regenerate
```

### Accounts App
```bash
python manage.py create_missing_profiles  # Create profiles for users
```

### Posts App
```bash
python manage.py expire_posts         # Mark expired posts inactive
python manage.py expire_posts --dry-run  # Test without changes
```

---

## Settings Structure

### Base Settings (base.py)
- Installed apps
- Middleware
- Templates
- Password validators
- Internationalization
- Static/media files
- Authentication settings

### Development Settings (development.py)
- DEBUG = True
- SQLite database
- Hardcoded SECRET_KEY
- Localhost allowed hosts

### Production Settings (production.py)
- DEBUG = False (from env)
- PostgreSQL database (from DATABASE_URL)
- SECRET_KEY from environment
- ALLOWED_HOSTS from environment
- Full security headers:
  - SECURE_SSL_REDIRECT
  - SESSION_COOKIE_SECURE
  - CSRF_COOKIE_SECURE
  - SECURE_HSTS_SECONDS
  - X_FRAME_OPTIONS

---

## Environment Variables

### Development
No environment variables needed. Uses default development settings.

### Production
Required in `.env` file:
```env
DJANGO_ENV=production
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@host:port/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

---

## Dependencies

```txt
Django==6.0.7              # Web framework
Pillow==12.3.0             # Image processing
django-environ==0.11.2     # Environment variables
psycopg2-binary==2.9.9    # PostgreSQL adapter
```

---

## Design System

### Colors
- Primary: Blue (#3b82f6)
- Neutral: Grays (#171717 to #fafafa)

### Spacing
- 8px spacing system
- Tailwind CSS utility classes

### Typography
- Font sizes: xs to 3xl
- Line heights: Optimized for readability

### Components
- Cards with soft borders
- Minimal shadows
- Rounded corners (xl, 2xl)
- Mobile-first responsive design

---

## Recent Implementations

### ✅ About Page
- Founder story and personal introduction
- Tech stack display
- Projects showcase
- GitHub connection

### ✅ Seed Data Command
- Generates 30 users with Indian names
- Creates 100 realistic posts
- Distributed across all categories
- Uses Pune locations

### ✅ Production Settings
- Environment-based configuration
- PostgreSQL support
- Full security headers
- Environment variables management

---

## Status

✅ **MVP**: Complete  
✅ **Authentication**: Complete  
✅ **Profiles**: Complete  
✅ **Posts CRUD**: Complete  
✅ **Search & Filters**: Complete  
✅ **Pagination**: Complete  
✅ **Post Expiry**: Complete  
✅ **UI Polish**: Complete  
✅ **Landing Page**: Complete  
✅ **About Page**: Complete  
✅ **Seed Data**: Complete  
✅ **Production Settings**: Complete  

🚀 **Overall Status**: Production Ready

---

## Quick Commands

```bash
# Development
python manage.py runserver
python manage.py seed_data
python manage.py makemigrations
python manage.py migrate

# Production
export DJANGO_ENV=production
python manage.py check --deploy
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py createsuperuser
gunicorn campushub.wsgi:application
```

---

## Next Steps

1. ✅ Development complete
2. ✅ Production configuration complete
3. 🎯 Deploy to production platform
4. 🎯 Set up domain and SSL
5. 🎯 Configure production database
6. 🎯 Launch to users

---

**Project**: CampusHub  
**Status**: Production Ready ✅  
**Date**: 2026-07-24  
**Documentation**: Complete
