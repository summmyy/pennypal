from rest_framework import serializers
from .models import Transaction, Budget, UserTotal, Income

class UserTotalSerializer(serializers.ModelSerializer):
   class Meta:
      model = UserTotal
      fields = '__all__' 

class IncomeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Income
      fields = '__all__' 

class TransactionSerializer(serializers.ModelSerializer):
   class Meta:
      model = Transaction
      fields = '__all__' 

class BudgetSerializer(serializers.ModelSerializer):
   class Meta:
      model = Budget
      fields = '__all__'