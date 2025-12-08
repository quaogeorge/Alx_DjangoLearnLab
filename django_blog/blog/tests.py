from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from django.urls import reverse

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('u', 'u@example.com', 'pass')
        self.post = Post.objects.create(title='t', content='c', author=self.user)

    def test_create_comment(self):
        self.client.login(username='u', password='pass')
        resp = self.client.post(reverse('blog:post_detail', kwargs={'pk': self.post.pk}), {'content': 'Nice post!'})
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(self.post.comments.count(), 1)