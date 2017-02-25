from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

EXPENSE_STATUSES = [
    ('N','New'),
    ('A','Approved'),
    ('D','Declined'),
    ('P','Paid'),
    ('I','Ignored'),
]

class ExpenseClaim(models.Model):
    """..."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users')
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
                        max_length=2,
                        choices=EXPENSE_STATUSES,
                        default='N'
                    )
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

class ExpensePhoto(models.Model):
    '''...'''
    claim = models.ForeignKey('ExpenseClaim', related_name='photos')
    photo = models.ImageField(blank=True, null=True)
    description = models.TextField()