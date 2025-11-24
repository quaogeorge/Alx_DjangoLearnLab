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