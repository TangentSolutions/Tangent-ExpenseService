from rest_framework import serializers
from .models import ExpenseClaim

from account.serializers import UserSerializer

class ExpenseClaimSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = ExpenseClaim
        fields = ('name', 'description', 'status', 'user', 'id', 'photos')
        depth = 1

class ExpenseClaimListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseClaim
        fields = ('name', 'id',)


