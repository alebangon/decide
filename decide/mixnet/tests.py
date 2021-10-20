from django.test import TestCase
from django.conf import settings
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from mixnet.mixcrypt import MixCrypt
from mixnet.mixcrypt import ElGamal

from base import mods


class MixnetCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)

    def tearDown(self):
        self.client = None

    def encrypt_msgs(self, msgs, pk, bits=settings.KEYBITS):
        p, g, y = pk
        k = MixCrypt(bits=bits)
        k.k = ElGamal.construct((p, g, y))

        cipher = [k.encrypt(i) for i in msgs]
        return cipher
