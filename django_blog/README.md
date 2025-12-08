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

 # Tagging System
- Add tags when creating/editing a post using comma-separated values.
- Tags turn into clickable links on the post detail page.
- Clicking a tag filters posts by that tag.

# Search
- Search bar at the top accepts keywords.
- Search looks in post title, content, and tag names.
- Results displayed on /search/?q=<term>.