# IBM_CHALLENGE

Simple Django example project used for demonstrating a small text-analysis web app and related notebooks.

## Overview

This repository contains a minimal Django application (`challenge_ibm`) that provides a web UI to analyze text and some accompanying Jupyter notebooks and static assets. It includes Docker-related files for containerized runs and a `requirements.txt` for a Python virtual environment installation.

Key pieces:
- `manage.py` — Django management entrypoint.
- `challenge_ibm/` — Django application with views, URL mappings, settings and static/templates.
- `notebooks/` — Jupyter notebooks with experiments (classification and summarization examples).
- `requirements.txt` — Python dependencies.
- `Dockerfile`, `docker-compose.yml`, `nginx.conf` — optional container orchestration and deployment helpers.

## Features

- Home page served from `challenge_ibm/templates/index.html`.
- A simple analysis endpoint at `/analyze/` (mapped to `views.analyze_text`) which accepts text input from the UI and returns an analysis result.
- Static assets (CSS, JS, images) in `challenge_ibm/statics/`.
- Example Jupyter notebooks in `notebooks/` for model experiments and results.

## Requirements

- Python 3.8+ (depending on packages in `requirements.txt`).
- pip.
- Docker and docker-compose (optional, for container runs).

## Quick start (PowerShell)

Create and activate a virtual environment, install dependencies, then run the Django dev server:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Open http://localhost:8000 in your browser to view the home page. The admin route is available at `/admin/` once you create a superuser.

## Run with Docker (optional)

If you prefer Docker, build and run the containers with docker-compose (requires Docker and docker-compose installed):

```powershell
docker-compose up --build
```

This will build the app image and bring up any defined services. Consult `docker-compose.yml` for service names and ports.

## Endpoints

- `/` — Home page (`challenge_ibm.views.home`).
- `/analyze/` — Text analysis endpoint (`challenge_ibm.views.analyze_text`).
- `/admin/` — Django admin site.

Example usage (browser): open the home page, enter text and submit to `/analyze/`.

Example usage (curl):

```powershell
curl -Method POST -Uri http://localhost:8000/analyze/ -Body @{ text = 'Some text to analyze' }
```

Note: the exact POST payload accepted by `analyze_text` depends on the view implementation.

## Project structure (high level)

- `manage.py` — Django entrypoint.
- `challenge_ibm/` — Django app:
  - `__init__.py`, `asgi.py`, `wsgi.py`, `settings.py` — Django config and app bootstrap.
  - `urls.py` — URL patterns (`/`, `/analyze/`, `/admin/`).
  - `views.py` — Request handlers including `home` and `analyze_text`.
  - `statics/` — static assets (`css/styles.css`, `js/main.js`, etc.).
  - `templates/` — HTML templates (e.g., `index.html`).
- `notebooks/` — Jupyter notebooks for experiments and result artifacts.

## Notebooks and models

See `notebooks/sum/` and `notebooks/classif/` for example notebooks. These contain experiments and model fine-tuning steps used during development but are not required to run the web app.

## Troubleshooting

- If static files don't load in development, ensure `DEBUG = True` in `challenge_ibm/settings.py` or run `python manage.py collectstatic` in production mode with appropriate static root settings.
- If migrations fail, run `python manage.py makemigrations` and `python manage.py migrate`.
- If a dependency is missing, verify `requirements.txt` and install with `pip install -r requirements.txt`.

## Contributing

Small fixes and documentation updates are welcome. If you add features, document new endpoints or settings in this README.

## License

This repository does not include a license file; add one if you plan to publish or share the project with others.
