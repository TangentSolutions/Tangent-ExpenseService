from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__' #('url', 'username', 'email', 'is_staff')
        exclude = ('password',)

