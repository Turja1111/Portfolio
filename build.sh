#!/usr/bin/env bash
# Render build script — runs on every deploy

set -o errexit  # Exit on any error

# Install Python dependencies
pip install -r requirements.txt

# Collect static files (WhiteNoise serves them)
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
