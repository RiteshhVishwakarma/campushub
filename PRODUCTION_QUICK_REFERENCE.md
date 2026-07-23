# Production Quick Reference

## Seed Data Commands

### Generate Development Data
```bash
python manage.py seed_data
```
Creates:
- 30 users (seed_user_1 to seed_user_30)
- 100 realistic posts across all categories
- Test password: `seedpass123`

### Clear and Regenerate
```bash
python manage.py seed_data --clear
```

---

## Environment Configuration

### Development (Default)
No configuration needed. Just run:
```bash
python manage.py runserver
```

### Production Setup

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Create .env File**
```bash
# Copy template
copy .env.example .env

# Edit .env and fill in:
DJANGO_ENV=production
SECRET_KEY=your-generated-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@host:port/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

3. **Generate Secret Key**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

4. **Run Migrations**
```bash
python manage.py migrate
```

5. **Collect Static Files**
```bash
python manage.py collectstatic --no-input
```

6. **Create Superuser**
```bash
python manage.py createsuperuser
```

7. **Run Production Server**
```bash
# Install gunicorn first
pip install gunicorn

# Run
gunicorn campushub.wsgi:application
```

---

## Settings Structure

```
campushub/settings/
├── __init__.py         # Auto-loads based on DJANGO_ENV
├── base.py             # Common settings
├── development.py      # Dev: DEBUG=True, SQLite
└── production.py       # Prod: DEBUG=False, PostgreSQL
```

**Auto-selection**:
- `DJANGO_ENV=production` → production.py
- `DJANGO_ENV=development` or not set → development.py

---

## Database URLs

### PostgreSQL
```
DATABASE_URL=postgres://user:password@localhost:5432/campushub
```

### SQLite (Development Only)
Automatically configured in development.py

---

## Common Issues

### Module not found: environ
```bash
pip install django-environ
```

### Module not found: psycopg2
```bash
pip install psycopg2-binary
```

### Settings import error
Check `campushub/settings/__init__.py` exists

---

## Deployment Platforms

### Heroku
```bash
heroku config:set DJANGO_ENV=production
heroku config:set SECRET_KEY=your-key
heroku config:set DEBUG=False
# DATABASE_URL auto-set by Heroku
```

### Railway/Render
Set in dashboard:
- `DJANGO_ENV=production`
- `SECRET_KEY=...`
- `DEBUG=False`
- `ALLOWED_HOSTS=...`

---

## Files Changed

✅ Created: `campushub/settings/` directory  
✅ Created: `.env.example`  
✅ Created: `core/management/commands/seed_data.py`  
✅ Updated: `requirements.txt`  
✅ Backed up: `settings.py` → `settings.py.backup`  

---

## Safety Notes

- ✅ No business logic changed
- ✅ No UI modified
- ✅ No routes changed
- ✅ Backward compatible
- ✅ Development workflow unchanged
- ✅ Seed data safe to run multiple times

---

## Quick Test

```bash
# 1. Check system
python manage.py check

# 2. Generate seed data
python manage.py seed_data

# 3. Run server
python manage.py runserver

# 4. Visit http://localhost:8000
# 5. Login: seed_user_1 / seedpass123
```

---

**Status**: ✅ Ready for Development and Production
