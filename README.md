# CampusHub

A Django-based student community platform for discovering roommates, flats, internships, events, and marketplace listings.

## 🚀 Status: Production Ready

CampusHub is fully developed and production-ready with proper environment configuration, security measures, and development tooling.

---

## Features

### Core Functionality
- **User Authentication**: Registration, login, logout with profile management
- **Post Management**: Create, read, update, delete posts across 5 categories
- **Categories**: Roommate, Flat/PG, Events, Internship, Buy & Sell
- **Search & Filters**: Search by title/description, filter by category and location
- **Pagination**: 15 posts per page with filter preservation
- **Post Expiry**: Automatic 30-day expiry system
- **Profile System**: User profiles with photos, bio, phone, and college info
- **Image Uploads**: Support for profile photos and post images
- **Responsive Design**: Mobile-first with Tailwind CSS

### Additional Features
- Realistic seed data generation (30 users + 100 posts)
- Production-ready settings structure
- Environment-based configuration
- PostgreSQL support for production
- Full security headers
- Clean, minimal UI design

---

## Quick Start

### Development Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd campushubadypu
```

2. **Create virtual environment**
```bash
python -m venv env

# Windows
env\Scripts\activate

# Linux/Mac
source env/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Generate seed data (optional but recommended)**
```bash
python manage.py seed_data
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Visit: `http://localhost:8000`
- Login with: `seed_user_1` / `seedpass123`

---

## Production Deployment

### Prerequisites
- Python 3.8+
- PostgreSQL database
- Web server (Nginx/Apache)
- WSGI server (Gunicorn/uWSGI)

### Setup Steps

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Create .env file**
```bash
cp .env.example .env
# Edit .env with your production values
```

3. **Generate SECRET_KEY**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

4. **Set environment variables in .env**
```env
DJANGO_ENV=production
SECRET_KEY=your-generated-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@host:port/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

5. **Run migrations**
```bash
export DJANGO_ENV=production  # Windows: set DJANGO_ENV=production
python manage.py migrate
```

6. **Collect static files**
```bash
python manage.py collectstatic --no-input
```

7. **Create superuser**
```bash
python manage.py createsuperuser
```

8. **Run with Gunicorn**
```bash
pip install gunicorn
gunicorn campushub.wsgi:application
```

For detailed deployment instructions, see [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)

---

## Project Structure

```
campushubadypu/
├── campushub/              # Main project configuration
│   └── settings/           # Environment-based settings
│       ├── base.py         # Common settings
│       ├── development.py  # Development settings
│       └── production.py   # Production settings
├── core/                   # Landing and about pages
├── accounts/               # User authentication & profiles
├── posts/                  # Posts functionality
├── static/                 # Static files (CSS, JS)
├── media/                  # User uploads
├── templates/              # HTML templates
└── requirements.txt        # Python dependencies
```

---

## Management Commands

### Seed Data
```bash
# Generate realistic development data (30 users + 100 posts)
python manage.py seed_data

# Clear existing seed data and regenerate
python manage.py seed_data --clear
```

### Post Expiry
```bash
# Mark expired posts (>30 days) as inactive
python manage.py expire_posts

# Dry run (show what would be expired)
python manage.py expire_posts --dry-run
```

### Profile Management
```bash
# Create profiles for users missing them
python manage.py create_missing_profiles
```

---

## Tech Stack

- **Backend**: Django 6.0.7
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Image Processing**: Pillow
- **Environment Management**: django-environ
- **Database Adapter**: psycopg2-binary (PostgreSQL)

---

## Environment Configuration

### Development (Default)
- DEBUG mode enabled
- SQLite database
- Runs on `localhost:8000`
- No environment variables needed

### Production
- DEBUG mode disabled
- PostgreSQL database
- Full security headers
- Environment variables required

---

## Security Features

### Production Security (Automatic)
- SSL/HTTPS enforcement
- Secure session cookies
- Secure CSRF cookies
- XSS protection
- Content type sniffing protection
- Clickjacking protection (X-Frame-Options)
- HSTS with preload
- Environment-based secrets

---

## Database Models

### User (Django Built-in)
Standard Django user model

### Profile
- Extended user information
- Phone, bio, college, profile photo
- Auto-created via signals

### Post
- Title, description, category
- Price (optional), location, phone
- Image upload support
- 30-day expiry system

### Report
- Flag inappropriate posts
- Multiple report reasons
- One report per user per post

---

## URL Routes

```
/                              Landing page
/about/                        About page
/accounts/register/            User registration
/accounts/login/               User login
/accounts/profile/<username>/  User profile
/posts/                        Browse posts
/posts/create/                 Create post
/posts/<id>/                   Post detail
/admin/                        Admin panel
```

---

## Documentation

Complete documentation available:

- **[PRODUCTION_READY_COMPLETE.md](PRODUCTION_READY_COMPLETE.md)** - Complete production guide
- **[PRODUCTION_QUICK_REFERENCE.md](PRODUCTION_QUICK_REFERENCE.md)** - Quick command reference
- **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Step-by-step deployment
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Detailed project structure
- **[FINAL_IMPLEMENTATION_SUMMARY.md](FINAL_IMPLEMENTATION_SUMMARY.md)** - Implementation summary

---

## Testing Credentials

After running `python manage.py seed_data`:

- **Username**: `seed_user_1` to `seed_user_30`
- **Password**: `seedpass123`

---

## Development Workflow

```bash
# Start development server
python manage.py runserver

# Generate seed data
python manage.py seed_data

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run Django shell
python manage.py shell
```

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## Support

For issues, questions, or contributions:
- Check documentation files
- Review deployment checklist
- Consult quick reference guide

---

## License

This project is for educational purposes.

---

## Author

**Ritesh Vishwakarma**  
BCA Student • Full Stack Developer

Building practical products that solve real student problems.

- GitHub: [@rietshhvishwakarma](https://github.com/rietshhvishwakarma)

---

## Acknowledgments

Built with Django and modern web technologies to serve the student community.

---

**Project Status**: ✅ Production Ready  
**Last Updated**: 2026-07-24
