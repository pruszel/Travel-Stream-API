# Travel Stream API

REST API for the [Travel Stream web app](https://travelstreamapp.com) available at [api.travelstreamapp.com](https://api.travelstreamapp.com).

## Development

The API is built with [Django](https://www.djangoproject.com/). Two Django apps are set up: `users` for user auth and `dashboard` for the trip data users will be interacting with through the dashboard UI.

### Requirements

- python 3.10 and pip

### Installation

- Load the Python virtual environment: `source .venv/bin/activate`
- Install python dependencies: `pip install -r requirements.txt`

### Set up

- Load the Python virtual environment: `source .venv/bin/activate`
- Create a local environment variable file by copying the example file and changing the values: `cp .env.example .env`
- Start the Django development server: `python manage.py runserver`

### Tests

- Load the Python virtual environment: `source .venv/bin/activate`
- Run pytest: `pytest`

## Deployment

The API is deployed with Fly.io.

### Requirements

- Fly.io CLI

### Set up

- Set environment variables: `fly secrets set`
  - [`SECRET_KEY` Django setting](https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-SECRET_KEY)
  - [`SECURE_PROXY_SSL_HEADER` Django setting](https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER)
  - [`SECURE_SSL_REDIRECT` Django setting](https://docs.djangoproject.com/en/5.1/ref/settings/#secure-ssl-redirect)
  - [`USE_X_FORWARDED_HOST` Django setting](https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-USE_X_FORWARDED_HOST)

### Process

- A GitHub Action will deploy new commits on `main` to Fly.io automatically.
