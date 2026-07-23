# CampusHub - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Python 3.14+ installed
- Virtual environment activated

### Installation

1. **Activate Virtual Environment**
```bash
# Windows
.\env\Scripts\activate

# Linux/Mac
source env/bin/activate
```

2. **Verify Installation**
```bash
python manage.py check
```

3. **Run Development Server**
```bash
python manage.py runserver
```

4. **Access the Application**
Open your browser and visit:
```
http://127.0.0.1:8000/
```

## 📱 Application URLs

### Public Pages
- **Home:** http://127.0.0.1:8000/
- **Browse Posts:** http://127.0.0.1:8000/posts/
- **Login:** http://127.0.0.1:8000/accounts/login/
- **Register:** http://127.0.0.1:8000/accounts/register/

### Authenticated Pages
- **Create Post:** http://127.0.0.1:8000/posts/create/
- **Logout:** http://127.0.0.1:8000/accounts/logout/

### Admin Panel
- **Admin:** http://127.0.0.1:8000/admin/
  - Create superuser: `python manage.py createsuperuser`

## 🎨 Features Currently Available

### ✅ Working Features
1. **User Registration**
   - Navigate to Register page
   - Fill in username and password
   - Automatically logged in after registration

2. **User Login/Logout**
   - Login with credentials
   - Session management
   - Logout functionality

3. **Navigation**
   - Mobile-responsive top navigation
   - Bottom navigation bar (mobile)
   - Active page highlighting

4. **Home Page**
   - Hero section
   - Category cards
   - Responsive layout

5. **Browse Posts Page**
   - Category filters
   - Placeholder for posts

### ⏳ Pending Implementation (Next Phase)
- Post models
- Post creation with forms
- Post listing with data
- Post detail views
- Image uploads
- Search and filtering
- User profiles

## 🛠️ Development Commands

### Run Server
```bash
python manage.py runserver
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Make Migrations (After model changes)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Tests
```bash
python manage.py test
```

### Collect Static Files (Production)
```bash
python manage.py collectstatic
```

## 📦 Project Structure Overview

```
campushubadypu/
├── accounts/          # User authentication
├── core/              # Home and core pages
├── posts/             # Post management
├── templates/         # HTML templates
├── static/            # CSS, JS, images
└── media/             # User uploads
```

## 🎯 Testing the Application

### Test User Registration
1. Go to http://127.0.0.1:8000/accounts/register/
2. Enter a username (e.g., "testuser")
3. Enter a password (must meet Django requirements)
4. Confirm password
5. Click "Create Account"
6. You should be redirected to home page as logged-in user

### Test User Login
1. Go to http://127.0.0.1:8000/accounts/login/
2. Enter your username
3. Enter your password
4. Click "Sign In"
5. Check top-right corner for user initial

### Test Navigation
1. Click on different navigation items
2. Notice active state highlighting
3. Test on mobile view (resize browser or use DevTools)
4. Bottom navigation should appear on mobile

### Test Browse Posts
1. Click "Browse" in navigation
2. See category filter buttons
3. Notice placeholder message (posts not yet implemented)

## 🔧 Troubleshooting

### Server won't start
```bash
# Check for errors
python manage.py check

# Ensure migrations are applied
python manage.py migrate
```

### Static files not loading
```bash
# Verify settings
python manage.py findstatic css/style.css
```

### Template not found
- Check DIRS in TEMPLATES setting
- Verify template path matches URL pattern

## 📝 Next Steps

Wait for the next instruction to:
1. Create Post and Category models
2. Implement post creation forms
3. Display posts with filtering
4. Add image uploads
5. Implement contact functionality

---

**Ready to develop!** 🎉

The foundation is solid and ready for the next phase of development.
