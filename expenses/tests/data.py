from expenseservice import testutils
from ..models import ExpenseClaim, ExpensePhoto, EXPENSE_STATUSES
from faker import Factory
import random

FAKE = Factory.create()

def create_fake_expense_claim(user=None, password="testtest", **kwargs):
    """Creates a fake user"""

    if user is None:
        user = testutils.create_fake_user()

    data = {
        'user': user,
        'name': FAKE.bs(),
        'description': FAKE.paragraph(),
        'status': random.choice(EXPENSE_STATUSES)[0]
    }
    data.update(kwargs)

    return ExpenseClaim.objects.create(**data)

def create_claims_with_photos(claim=None, num_photos=3, **kwargs):
    if claim is None:
        claim = create_fake_expense_claim()

    for x in range(0,3):
        data = {
            'claim_id': claim.id,
            'description': FAKE.paragraph()
        }
        data.update(kwargs)
        ExpensePhoto.objects.create(**data)
    return claim
