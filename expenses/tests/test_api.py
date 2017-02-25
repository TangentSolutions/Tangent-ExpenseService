from django.test import TestCase, Client
from unittest import skip, skipIf
from django.conf import settings

class APITestCase(TestCase):

    def setUp(self):
        pass

    @skipIf(not settings.FAIL_IF_TODO, "Not yet implemented")
    def test_ok(self):
        self.fail()

    @skipIf(not settings.FAIL_IF_TODO, "Not yet implemented")
    def test_ok(self):
        self.fail()

class APIListTestCase(TestCase):

    def setUp(self):
        pass

    @skip("Not yet implemented")
    def test_can_filter_on_status(self):
        pass


class APIDetailTestCase(TestCase):

    def setUp(self):
        pass

    @skip("Not yet implemented")
    def test_get_expense(self):
        pass

    @skip("Not yet implemented")
    def test_get_expense_contains_list_of_photos(self):
        pass