#!/usr/bin/env bash
# Render build script: install deps, collect static files, migrate the DB
# and (optionally) load demo data the first time the database is empty.
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate --no-input

if [ "${SEED_DEMO_DATA:-false}" = "true" ]; then
    if python manage.py shell -c "import sys; from posts.models import Post; sys.exit(0 if Post.objects.exists() else 1)"; then
        echo "Posts already exist, skipping demo seed."
    else
        echo "Empty database, loading demo data..."
        python manage.py seed_data
    fi
fi
