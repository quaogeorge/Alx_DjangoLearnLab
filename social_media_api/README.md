# Social Media API (initial)

## Overview
Simple Django REST API that implements user registration, login (token), and basic profile.

## Setup
1. Create virtualenv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

POST /api/posts/
GET /api/posts/
GET /api/posts/{id}/
PATCH /api/posts/{id}/
DELETE /api/posts/{id}/

POST /api/comments/
GET /api/comments/
PATCH /api/comments/{id}/
DELETE /api/comments/{id}/   

### Follow Users
POST /api/accounts/follow/{user_id}/
POST /api/accounts/unfollow/{user_id}/

### Feed
GET /api/feed/
Returns posts from users the authenticated user follows.
Posts are ordered from newest to oldest.

## Deployment

The Social Media API is deployed on Heroku.

### Live URL
https://social-media-api-kojo.herokuapp.com

### Deployment Steps
- Configured Django for production
- Used Gunicorn as WSGI server
- Used WhiteNoise for static files
- PostgreSQL database via Heroku
- Environment variables for secrets

### Maintenance
- Logs monitored via Heroku dashboard
- Dependencies updated via requirements.txt