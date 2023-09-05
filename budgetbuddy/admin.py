from django.contrib import admin
from .models import UserTotal, Income, Budget, Transaction
# Register your models here.
admin.site.register(UserTotal)
admin.site.register(Income)
admin.site.register(Transaction)
admin.site.register(Budget)