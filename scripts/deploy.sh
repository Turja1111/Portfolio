#!/bin/bash
set -euo pipefail

# ── Configuration ─────────────────────────────────────────────────
DOCKER_USERNAME="${DOCKER_USERNAME:-yourusername}"
IMAGE_NAME="${IMAGE_NAME:-portfolio}"
COMPOSE_FILE="docker-compose.prod.yml"

echo "🚀 Starting deployment..."

# Pull latest image
echo "📦 Pulling latest Docker image..."
docker pull "${DOCKER_USERNAME}/${IMAGE_NAME}:latest"

# Run migrations
echo "🗄️  Running database migrations..."
docker compose -f "${COMPOSE_FILE}" exec -T web python manage.py migrate --noinput

# Collect staticfiles
echo "📁 Collecting static files..."
docker compose -f "${COMPOSE_FILE}" exec -T web python manage.py collectstatic --noinput

# Restart services
echo "🔄 Restarting containers..."
docker compose -f "${COMPOSE_FILE}" up -d --no-deps web nginx

# Health check
echo "❤️  Health check..."
sleep 5
if curl -sSf http://localhost > /dev/null 2>&1; then
  echo "✅ Deployment successful! Site is up."
else
  echo "⚠️  Site may not be responding — check logs with: docker compose -f ${COMPOSE_FILE} logs web"
fi
