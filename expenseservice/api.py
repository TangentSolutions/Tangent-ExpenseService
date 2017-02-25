from rest_framework import routers
from account.api import UserViewSet
from expenses.api import ExpenseClaimViewSet

router = routers.DefaultRouter()

# expenses
router.register(r'expenses', ExpenseClaimViewSet)

# account
router.register(r'users', UserViewSet)