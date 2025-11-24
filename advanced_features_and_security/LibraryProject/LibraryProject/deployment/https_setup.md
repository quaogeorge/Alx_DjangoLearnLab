# HTTPS Deployment Configuration

To run the Django application securely in production:

## 1. Obtain SSL/TLS Certificates
Use one of the following:
- Let’s Encrypt (recommended)
- Cloudflare SSL
- Purchased certificate from a CA

For Let’s Encrypt:

## 2. Nginx Configuration Example

server_name yourdomain.com www.yourdomain.com;

ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

ssl_protocols TLSv1.2 TLSv1.3;

location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto https;
}

## 3. Required Django Settings
(These are already added in settings.py)

- SECURE_SSL_REDIRECT = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True

## 4. Testing HTTPS
Use:
- https://www.ssllabs.com/ssltest/ (SSL config)
- Browser devtools → Network tab → ensure HTTPS and security headers are active