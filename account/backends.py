from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

class SimpleBackend(object):
    """
    A simple authentication backend
    """

    def authenticate(self, username=None, password=None):
        if username == 'joe' and password == 'testtest':
            return get_user_model().objects.first()
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None