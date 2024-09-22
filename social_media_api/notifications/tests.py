# notifications/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification

class NotificationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.other_user = User.objects.create_user(username='otheruser', password='12345')

    def test_fetch_notifications(self):
        Notification.objects.create(
            recipient=self.user,
            actor=self.other_user,
            verb='liked your post',
            target=self.other_user,
        )
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'liked your post')
