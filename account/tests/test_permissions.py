from django.test import TestCase, Client
from unittest import skip, skipIf
from django.conf import settings
import mock
from rest_framework.request import Request
from ..permissions import IsOwnerOrReadOnly
from expenseservice.testutils import create_fake_user

class OwnerOrReadOnlyTestCase(TestCase):

    def setUp(self):
        pass

    @mock.patch('rest_framework.request.Request')
    def test_object_permissions(self, mock_request):
        mock_request.method = 'GET'
        user = create_fake_user()
        perm = IsOwnerOrReadOnly()
        perm.has_object_permission(mock_request, None, user)





