from rest_framework import viewsets
from .models import ExpenseClaim
from .serializers import ExpenseClaimSerializer, ExpenseClaimListSerializer
from django.contrib.auth.models import User


class MultiSerializerMixin:

    def get_serializer_class(self):
        return self.serializer_map.get(
                        self.action,
                        self.serializer_class
                    )

class ExpenseClaimViewSet(MultiSerializerMixin, viewsets.ModelViewSet):
    queryset = ExpenseClaim.objects.all()
    # serializer_class = ExpenseClaimSerializer

    serializer_map = {
            "create": ExpenseClaimSerializer,
            "list": ExpenseClaimListSerializer,
            "retrieve": ExpenseClaimSerializer,
        }
