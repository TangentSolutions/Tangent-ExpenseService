from django.test import TestCase
from .data import create_fake_expense_claim
from ..serializers import ExpenseClaimSerializer, ExpenseClaimListSerializer

class ExpenseClaimSerializerTestCase(TestCase):

    def test_serialize_serializer(self):

        claim = create_fake_expense_claim()
        ExpenseClaimSerializer(claim).data

class ExpenseClaimListSerializerTestCase(TestCase):

    def setUp(self):
        claim = create_fake_expense_claim()
        self.data = ExpenseClaimListSerializer(claim).data

    def test_serialize_serializer_contains_name_field(self):
        assert self.data.get('name', None) is not None

    def test_serialize_serializer_doesnt_contain_other_fields(self):
        desc = self.data.get('description', None)
        assert desc is None, \
            'Expected description to be None. Got: {}' . format(desc)
