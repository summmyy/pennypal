from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class UserTotal(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    income_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    transaction_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    budget_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.user_id}'
    

    
class Income(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    source = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=datetime.now)
    income_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.amount} - {self.source}'

class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    date = models.DateField(auto_now_add=datetime.now)
    category = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=255, default='')
    transaction_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)


    def __str__(self):
        return f'{self.amount} - {self.category}'


class Budget(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    category = models.CharField(max_length=100, default='')
    allocated_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    time_period = models.CharField(max_length=100, default='')
    budget_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)


    def __str__(self):
        return f'{self.allocated_amount} - {self.category}'


