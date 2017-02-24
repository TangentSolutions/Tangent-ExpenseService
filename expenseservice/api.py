from rest_framework import routers
from account.api import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)