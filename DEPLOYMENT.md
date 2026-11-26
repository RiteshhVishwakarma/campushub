# Deployment

## Render (recommended)

`render.yaml` is a Render Blueprint. It creates the web service and a free PostgreSQL database.

1. Push the code to GitHub (branch `main`).
2. In the Render dashboard, choose **New → Blueprint** and pick this repo.
3. When Render asks, enter the three Cloudinary values: `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY` and `CLOUDINARY_API_SECRET`.
4. Deploy. After that, every push to `main` redeploys the site.

On every deploy, `build.sh` installs the requirements, runs `collectstatic` and runs `migrate`. If `SEED_DEMO_DATA=true` and the database has no posts yet, it also loads the demo data.

You don't have to set `SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS` or `CSRF_TRUSTED_ORIGINS` on Render. The Blueprint generates or links the first two, and the production settings add the Render hostname from `RENDER_EXTERNAL_HOSTNAME` to the other two.

To create an admin user, open the service **Shell** on Render and run `python manage.py createsuperuser`.

## Environment variables

Production reads these from the environment or from a `.env` file. Copy `.env.example` as a starting point.

| Variable | Required | Notes |
|---|---|---|
| `DJANGO_ENV` | yes | `production` (otherwise the development settings load) |
| `SECRET_KEY` | yes | Generate one with `python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"` |
| `DEBUG` | yes | `False` |
| `DATABASE_URL` | yes | e.g. `postgres://user:pass@host:5432/campushub` |
| `ALLOWED_HOSTS` | off Render | Comma-separated domains |
| `CSRF_TRUSTED_ORIGINS` | off Render | Comma-separated, with `https://` |
| `CLOUDINARY_CLOUD_NAME` / `_API_KEY` / `_API_SECRET` | yes | Storage for uploaded profile and post photos |
| `SEED_DEMO_DATA` | no | `true` loads demo data on the first deploy |

Never commit `.env`. It is already in `.gitignore`.

## Other hosts

```bash
pip install -r requirements.txt
export DJANGO_ENV=production        # plus the variables above
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn campushub.wsgi:application
```

Put a reverse proxy with HTTPS in front of Gunicorn. The production settings force HTTPS and secure cookies, and turn on HSTS.

## Post expiry

Posts don't expire on their own schedule. To mark posts older than 30 days as inactive, run `python manage.py expire_posts` once a day, for example as a Render Cron Job or a crontab entry.
