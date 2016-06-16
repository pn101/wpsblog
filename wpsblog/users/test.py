from django.test import TestCase
from django.contrib.auth.models import User

from users.models.user_profile import UserProfile


class UserProfileModelTestCase(TestCase):

    def test_user_and_user_profile_link(self):
        test_username = 'username'
        test_password = 'password'
        test_email = 'p@p.com'

        test_user = User.objects.create_user(
                username=test_username,
                password=test_password,
                email=test_email,
        )

        self.assertTrue(
                test_user.userprofile
        )
