from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver


class Budget:

    name = models.CharField(max_length=30, default='Untitled')
    total_budget = models.DecimalField(max_digits=6, decimal_places=20)
    remaining_budget = models.DecimalField(max_digits=6, decimal_places=20)


class Transaction:
    id = 
    TYPE = (
            ('withdrawal', 'WITHDRAWAL'),
            ('deposit', 'DEPOSIT')
    )
    budget = models.ForeignKey(Budget)
    description = models.TextField()
    type = models.CharField(choices=TYPE)

