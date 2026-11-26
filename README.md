# CampusHub

### 🔗 Live demo: **[campushub-s4fd.onrender.com](https://campushub-s4fd.onrender.com/)**

Try it with the sample login: `seed_user_1` / `seedpass123`

> It runs on Render's free plan, so the first visit after a quiet spell can take about 30–60 seconds to load.

A Django site where students find roommates, flats/PGs, events and internships, and buy or sell things on campus.

## Features

- **Accounts:** register, log in and out, and a profile with photo, bio, phone and college
- **Posts** in 5 categories: Roommate, Flat / PG, Event, Internship, Buy & Sell
- **1 to 5 photos per post**, shown as a carousel on the post page (the first photo is the cover)
- **Search and filters** by keyword, category and location, 15 posts per page
- **Contact protection:** the phone number is masked until the visitor signs in
- **Reports:** signed-in users can flag a post, once per post
- **Auto-expiry:** posts expire 30 days after they are created
- Responsive layout with a mobile bottom nav

## Tech stack

Django 6 · SQLite (dev) / PostgreSQL (prod) · Cloudinary (uploaded images in prod) · WhiteNoise (static files) · Gunicorn · Tailwind CSS

## Run locally

**Windows, one click:** double-click `run_campushub.bat`. It creates the virtualenv, installs packages, runs migrations, loads sample data the first time and opens http://127.0.0.1:8000.

**Manual:**

```bash
python -m venv env
env\Scripts\activate          # macOS/Linux: source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data    # optional sample data
python manage.py runserver
```

You don't need a `.env` file for development. The dev settings use SQLite and save uploads in `media/`.

**Sample login** (after `seed_data`): `seed_user_1` … `seed_user_30`, password `seedpass123`.

## Management commands

| Command | What it does |
|---|---|
| `python manage.py seed_data` | Creates 30 users and 100 posts with photos (`--clear` removes them first) |
| `python manage.py expire_posts` | Marks posts older than 30 days as inactive (`--dry-run` only shows which ones) |
| `python manage.py create_missing_profiles` | Creates a profile for any user that has none |
| `python manage.py test` | Runs the tests |

## Project layout

```
campushub/settings/   base.py, development.py, production.py (picked with DJANGO_ENV)
core/                 home and about pages, seed_data command
accounts/             registration, login, profiles
posts/                posts, photos, reports, expire_posts command
templates/            HTML templates, one folder per app
static/               CSS and images
media/posts/          sample photos used by seed_data
```

## Data models

- **Profile:** one per user, created automatically. Holds phone, bio, college and profile photo.
- **Post:** category, title, description, optional price, location, phone, cover `image` and `is_active`.
- **PostImage:** the extra photos of a post (up to 4 more), in order.
- **Report:** a user flags a post with a reason. Each user can report a post only once.

## Main URLs

| URL | Page |
|---|---|
| `/` · `/about/` | Home, About |
| `/accounts/register/` · `/accounts/login/` | Sign up, sign in |
| `/accounts/profile/` · `/accounts/profile/edit/` | Your profile |
| `/posts/` · `/posts/create/` · `/posts/my-posts/` | Browse, new post, your posts |
| `/posts/<id>/` (`/edit/`, `/delete/`, `/report/`) | A post and its actions |
| `/admin/` | Django admin |

## Deployment

The site deploys to Render from `render.yaml`. See [DEPLOYMENT.md](DEPLOYMENT.md).

## Author

**Ritesh Vishwakarma** · [GitHub](https://github.com/RiteshhVishwakarma)

This project is for educational use.
