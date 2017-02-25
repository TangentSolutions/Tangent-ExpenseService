"""
Various utilities for making testing easier
"""
from faker import Factory
from django.contrib.auth import get_user_model
import random

FAKE = Factory.create()

def assert_response(response, expected_status=200):
    """
    Asserts the responses status code matches expectations
    Prints a nice assertion error if not
    """

    assert response.status_code == expected_status, \
        'Expected status: {}. Got: {}: {}' . format(
            expected_status,
            response.status_code,
            response.content)

def assert_num_results_returned(response, expected_count=0):
    """
    Assert that a paginated list endpoint returns the expected amount of results
    """
    actual_count = response.json().get('count')
    assert actual_count == expected_count, \
        'Expected {}. Got: {}. {}' . format(
            expected_count,
            actual_count,
            response.content
        )

## Data:

def random_phone_number():
    """Return a random phone number"""
    return "+27{}" . format(random.randint(100000000, 999999999))

def get_response_data(response):
    """
    Returns the data object from the response
    """
    return response.json().get('results')

def create_fake_user(password="testtest", **kwargs):
    """Creates a fake user"""

    return get_user_model().objects.create_user(
        username = kwargs.get('username', FAKE.user_name()),
        email=kwargs.get('email', FAKE.email()),
        password=kwargs.get('password', password),
        first_name=kwargs.get('first_name', FAKE.first_name()),
        last_name=kwargs.get('last_name', FAKE.last_name()),
    )

def create_fake_admin_user(password='testtest', **kwargs):
    return get_user_model().objects.create_superuser(
        username = kwargs.get('username', FAKE.user_name()),
        email=kwargs.get('email', FAKE.email()),
        password=kwargs.get('password', password),
        first_name=kwargs.get('first_name', FAKE.first_name()),
        last_name=kwargs.get('last_name', FAKE.last_name()),
    )

"""
def create_fake_staff_user(password='testtest', **kwargs):
    user = create_fake_user(password, **kwargs)
    import ipdb;ipdb.set_trace()
    user.is_staff = True
    user.save()
    return user
"""
