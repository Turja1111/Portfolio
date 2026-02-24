# ── Stage: Build ────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# ── Stage: Final ────────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# Non-root user
RUN groupadd -r django && useradd -r -g django django

# Runtime deps only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

COPY . .

# Static files
RUN mkdir -p /app/staticfiles /app/media && \
    DJANGO_SETTINGS_MODULE=portfolio.settings.production \
    SECRET_KEY=build-time-placeholder \
    DATABASE_URL=sqlite:////tmp/build.db \
    python manage.py collectstatic --noinput || true

RUN chown -R django:django /app
USER django

EXPOSE 8000

COPY scripts/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
