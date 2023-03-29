from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    middle_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=32, validators=[MinLengthValidator(6)])
    
class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, )
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    
class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    