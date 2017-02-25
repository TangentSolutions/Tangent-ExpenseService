from django.test import TestCase, Client
from .data import create_fake_expense_claim
from ..models import ExpenseClaim

class TestCreateFakeExpenseClaim(TestCase):

    def test_create_fake_expense_claim(self):
        claim = create_fake_expense_claim()

        assert isinstance(claim, ExpenseClaim)

    def test_create_fake_expense_claim_with_kwargs(self):
        data = {
            "name": "some expense claim"
        }
        claim = create_fake_expense_claim(**data)

        assert claim.name == data.get('name'), \
            'Expected name to be: {}. Got: {}' . format(data.get('name'), claim.name)