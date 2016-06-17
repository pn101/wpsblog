from django.test import TestCase
from django.contrib.auth.models import User

from bitly.models import BitLink


class BitLinkModelTestCase(TestCase):

    def test_for_bitlink_shorten_hash_initialization(self):
        test_username = 'username'
        test_password = 'password'
        test_email = 'email'
        test_user = User.objects.create_user(
                username=test_username,
                password=test_password,
                email=test_email,
        )

        test_url = 'http://bbc.com'

        test_bitlink = BitLink.objects.create(
                user=test_user,
                original_url=test_url,
        )

        self.assertTrue(
                test_bitlink.shorten_hash
        )
