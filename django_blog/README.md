Comments
--------
- Model: blog.Comment (fields: post, author, content, created_at, updated_at)
- Create: post detail page (POST to /posts/<pk>/). Must be logged in.
- Edit: /comments/<pk>/edit/ (only comment author)
- Delete: /comments/<pk>/delete/ (only comment author)
Testing:
 - Run migrations
 - Register or use superuser
 - Create a post, visit the post detail page, post a comment, edit/delete it.