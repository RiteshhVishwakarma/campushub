# Deployment Checklist

## Pre-Deployment

### Code Preparation
- [x] Settings refactored to base/development/production
- [x] Environment variables configured
- [x] SECRET_KEY moved to environment
- [x] Database configured for production (PostgreSQL)
- [x] Security headers enabled
- [x] DEBUG set to False in production
- [x] ALLOWED_HOSTS configured
- [x] Static files configuration ready
- [x] Media files configuration ready

### Dependencies
- [x] requirements.txt updated
- [x] django-environ added
- [x] psycopg2-binary added
- [ ] Install on production: `pip install -r requirements.txt`

### Database
- [ ] PostgreSQL installed on production
- [ ] Database created
- [ ] Database user created with proper permissions
- [ ] DATABASE_URL environment variable set

### Environment Variables
- [ ] Create .env file (or set in platform dashboard)
- [ ] Set DJANGO_ENV=production
- [ ] Generate and set SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Set DATABASE_URL
- [ ] Set ALLOWED_HOSTS

---

## Deployment Steps

### 1. Initial Setup
```bash
# Clone repository
git clone <your-repo-url>
cd campushubadypu

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration
```bash
# Copy template
cp .env.example .env

# Generate secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Edit .env with generated key and other values
nano .env
```

### 3. Database Setup
```bash
# Set production environment
export DJANGO_ENV=production

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 4. Static Files
```bash
# Collect static files
python manage.py collectstatic --no-input
```

### 5. Test Production Settings
```bash
# Check for issues
python manage.py check --deploy

# Verify settings loaded correctly
python manage.py diffsettings
```

### 6. Start Production Server
```bash
# Install gunicorn
pip install gunicorn

# Run gunicorn
gunicorn campushub.wsgi:application --bind 0.0.0.0:8000
```

---

## Platform-Specific

### Heroku

```bash
# Login
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set DJANGO_ENV=production
heroku config:set SECRET_KEY=your-generated-key
heroku config:set DEBUG=False

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Open app
heroku open
```

**Procfile** (create if deploying to Heroku):
```
web: gunicorn campushub.wsgi:application
release: python manage.py migrate
```

### Railway

1. Connect GitHub repository
2. Set environment variables in dashboard:
   - `DJANGO_ENV=production`
   - `SECRET_KEY=...`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=...`
3. Add PostgreSQL plugin
4. Deploy automatically on push

### Render

1. Create new Web Service
2. Connect repository
3. Set environment variables:
   - `DJANGO_ENV=production`
   - `SECRET_KEY=...`
   - `DEBUG=False`
4. Add PostgreSQL database
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn campushub.wsgi:application`

### DigitalOcean / VPS

```bash
# SSH into server
ssh user@your-server-ip

# Install system dependencies
sudo apt update
sudo apt install python3-pip python3-venv postgresql nginx

# Setup PostgreSQL
sudo -u postgres psql
CREATE DATABASE campushub;
CREATE USER campushub_user WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE campushub TO campushub_user;
\q

# Setup application
cd /var/www
git clone <your-repo>
cd campushubadypu
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install gunicorn

# Create .env file
nano .env
# (fill in production values)

# Run migrations
export DJANGO_ENV=production
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py createsuperuser

# Setup Gunicorn systemd service
sudo nano /etc/systemd/system/campushub.service
```

**Gunicorn Service File**:
```ini
[Unit]
Description=CampusHub Gunicorn
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/campushubadypu
Environment="DJANGO_ENV=production"
ExecStart=/var/www/campushubadypu/env/bin/gunicorn --workers 3 --bind unix:/var/www/campushubadypu/campushub.sock campushub.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Start service
sudo systemctl start campushub
sudo systemctl enable campushub

# Configure Nginx
sudo nano /etc/nginx/sites-available/campushub
```

**Nginx Configuration**:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/campushubadypu;
    }
    
    location /media/ {
        root /var/www/campushubadypu;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/campushubadypu/campushub.sock;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/campushub /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Setup SSL (optional but recommended)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## Post-Deployment

### Verification
- [ ] Site loads successfully
- [ ] Static files serving correctly
- [ ] Media files upload/display working
- [ ] Database connections working
- [ ] Admin panel accessible
- [ ] User registration working
- [ ] Login/logout working
- [ ] Post creation working
- [ ] Image upload working
- [ ] Search functionality working
- [ ] Pagination working

### Security
- [ ] DEBUG is False
- [ ] SECRET_KEY is unique and secure
- [ ] HTTPS enabled (SSL certificate)
- [ ] Secure cookies enabled
- [ ] Security headers present
- [ ] Admin URL secured (optional: change from /admin/)
- [ ] Database credentials secure
- [ ] .env file not committed to git

### Performance
- [ ] Static files served efficiently
- [ ] Database queries optimized
- [ ] Media files accessible
- [ ] Page load times acceptable

### Monitoring
- [ ] Error logging configured
- [ ] Server monitoring setup
- [ ] Database backups scheduled
- [ ] Uptime monitoring (optional)

---

## Optional Enhancements

### Media File Storage
For production, consider using cloud storage:
- AWS S3
- DigitalOcean Spaces
- Cloudinary
- Backblaze B2

### Caching
Configure Redis for better performance:
```bash
pip install django-redis
```

### Email Configuration
Setup email backend for notifications:
- Gmail SMTP
- SendGrid
- Mailgun
- AWS SES

### Domain Setup
- [ ] Domain purchased
- [ ] DNS configured
- [ ] A records pointing to server
- [ ] SSL certificate installed

---

## Rollback Plan

If deployment fails:

1. **Database**: Keep backup before migration
```bash
# Backup
pg_dump campushub > backup.sql

# Restore if needed
psql campushub < backup.sql
```

2. **Code**: Keep previous version tagged
```bash
git tag -a v1.0 -m "Stable version before production deployment"
git push origin v1.0
```

3. **Environment**: Document working configuration

---

## Maintenance Commands

### Check System
```bash
python manage.py check --deploy
```

### View Logs (Heroku)
```bash
heroku logs --tail
```

### Run Migrations
```bash
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Collect Static Files
```bash
python manage.py collectstatic --no-input
```

### Django Shell
```bash
python manage.py shell
```

---

## Common Issues

### Static files not loading
```python
# Verify in settings
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
```
Run: `python manage.py collectstatic`

### Database connection errors
Check:
- DATABASE_URL format
- PostgreSQL running
- User permissions
- Database exists

### 500 errors
- Check DEBUG=False
- Check logs
- Verify ALLOWED_HOSTS
- Check SECRET_KEY is set

### Media files not uploading
- Check MEDIA_ROOT permissions
- Verify directory exists
- Check MEDIA_URL configuration

---

## Support Resources

- Django Documentation: https://docs.djangoproject.com/
- Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- django-environ: https://django-environ.readthedocs.io/

---

## Final Checklist

Before going live:
- [ ] All environment variables set correctly
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] Superuser created
- [ ] Test user registration
- [ ] Test post creation
- [ ] Test image upload
- [ ] Verify security headers
- [ ] Check error pages (404, 500)
- [ ] SSL certificate active
- [ ] Domain pointing correctly
- [ ] Backup strategy in place

---

**Status**: Ready for deployment 🚀

Follow this checklist step by step for a smooth deployment process.
