from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from bitly.models.bitly import BitLink


class BitLinkCreateViewTestCase(TestCase):

    def test_bitlink_create_view_should_generate_shorten_hash(self):
        test_original_url = "http://www.example.com"
        test_username = 'username'
        test_password = 'password'
        test_email = 'p@p.com'

        test_user = User.objects.create_user(
                username=test_username,
                password=test_password,
                email=test_email,
        )

        bitlink = BitLink.objects.create(
                user=test_user,
                original_url=test_original_url,
        )

        self.assertTrue(
                bitlink.shorten_hash
        )
