# posts/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

class LikeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(author=self.user, content='Test post')

    def test_like_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(f'/posts/{self.post.pk}/like/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Like.objects.filter(user=self.user, post=self.post).exists())

    def test_unlike_post(self):
        self.client.login(username='testuser', password='12345')
        Like.objects.create(user=self.user, post=self.post)
        response = self.client.post(f'/posts/{self.post.pk}/unlike/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Like.objects.filter(user=self.user, post=self.post).exists())
