from django.test import TestCase, Client, override_settings
from unittest import skip, skipIf
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from expenseservice.testutils import create_fake_user

class TestCase(TestCase):

    def setUp(self):
        create_fake_user()

    def test_authenticate(self):
        user = authenticate(username='joe', password='testtest')
        assert isinstance(user, get_user_model())

    @override_settings(AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend'])
    def test_if_not_enabled(self):
        user = authenticate(username='joe', password='testtest')
        assert user is None