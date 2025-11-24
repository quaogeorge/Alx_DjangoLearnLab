# Permissions & Groups (bookshelf app)

Overview
- Model: bookshelf.Book (custom permissions: can_view, can_create, can_edit, can_delete)
- Groups created: Viewers, Editors, Admins

Setup (one-time)
1. Install requirements (Pillow already for images if used).
2. Run migrations:
   python3 manage.py makemigrations
   python3 manage.py migrate

3. Create groups and assign permissions:
   python3 manage.py setup_groups

Admin
- Log in to /admin/
- You can view Groups and adjust permissions manually.
- You can also inspect Permissions (filter by app 'bookshelf').

Testing (manual)
1. Create three users (viewer_user, editor_user, admin_user).
2. In admin > Groups, add each user to the appropriate group:
   - viewer_user -> Viewers
   - editor_user -> Editors
   - admin_user -> Admins
3. Log in as each user and try:
   - GET /books/ (list) -> requires can_view
   - GET & POST /books/create/ -> requires can_create
   - GET & POST /books/<id>/edit/ -> requires can_edit
   - POST /books/<id>/delete/ -> requires can_delete

Notes
- Decorators used: @permission_required('bookshelf.can_edit', raise_exception=True)
- If a user lacks permission, they will get a 403 (PermissionDenied). You can customize the view to redirect instead.
- Superusers bypass permission checks.


Security hardening applied
--------------------------
1. DEBUG set to False in production. Use environment variables to toggle locally.
2. Cookies:
   - CSRF_COOKIE_SECURE = True
   - SESSION_COOKIE_SECURE = True
   These ensure cookies are only sent over HTTPS.
3. Browser protection headers:
   - SECURE_BROWSER_XSS_FILTER = True
   - X_FRAME_OPTIONS = 'DENY'
   - SECURE_CONTENT_TYPE_NOSNIFF = True
4. CSP:
   - Implemented either with django-csp or custom middleware. See settings.py for values.
5. CSRF:
   - All form templates include {% csrf_token %}.
   - AJAX requests must include X-CSRFToken header.
6. SQL Injection:
   - All DB access uses Django ORM or parameterized queries.
   - User input is validated via Django Forms.
7. Testing:
   - Create users and attempt to access protected views as different roles.
   - Use browser dev tools to verify CSP and other headers.