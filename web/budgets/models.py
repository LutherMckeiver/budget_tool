from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):

    """This creates the attributes for Budget"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget')
    name = models.CharField(max_length=30, default='Untitled')
    total_budgets = models.FloatField()
    remaining_budget = models.FloatField()


class Transaction(models.Model):
    """This creates the attributes for Transaction"""
    TYPE = (
            ('withdrawal', 'WITHDRAWAL'),
            ('deposit', 'DEPOSIT')
    )
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transaction')
    description = models.TextField(blank=True, null=True)
    choices = models.CharField(choices=TYPE, max_length=150)
    amount = models.FloatField()
