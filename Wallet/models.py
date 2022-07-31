from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=15,null=True)
    lastname=models.CharField(max_length=15,null=True)
    address=models.CharField(default=1,max_length=100,null=True)
    emails=models.EmailField(max_length=30,null=True)
    phonenumber=models.CharField(max_length=10,null=True)
    age=models.IntegerField(null=True)
    gender=models.TextChoices

    # def __str__(self):
    #     return self.firstname
        
class Wallet(models.Model):
    balance=models.BigIntegerField
    isactive=models.BooleanField(max_length=5)
    Customer=models.OneToOneField
    pin=models.SmallIntegerField
    currency=models.CharField(max_length=8)
    date_created=models.DateTimeField(default=datetime.now)

class Account(models.Model):
    account_number = models.IntegerField()
    account_name=models.CharField(max_length=14)
    account_type=models.CharField
    balance=models.IntegerField
    wallet=models.ForeignObject

class Transaction(models.Model):
    transaction_code = models.IntegerField
    transaction_amount = models.BigIntegerField
    transaction_charges = models.IntegerField
    transaction_date_time = models.DateTimeField
    origin_account = models.ForeignKey
    destination_account = models.ForeignKey
    Receipt = models.OneToOneField

class Card(models.Model):
    serial_number =models.IntegerField()
    date_issued = models.DateTimeField(datetime.now,auto_now=False)
    expiry_date=models.DateTimeField(datetime.now,auto_now=False)
    signature=models.ImageField
    Account=models.ForeignKey
    Wallet=models.ForeignKey
    issuer=models.CharField

class Thirdparty(models.Model):
    name=models.CharField
    currency=models.ForeignKey
    transaction_cost=models.IntegerField
    Account=models.OneToOneField

class Notification(models.Model):
    description=models.TextField
    title=models.CharField(max_length=8)
    recipient=models.ForeignKey
    read_unread_status=models.CharField
    date_and_time=models.DateTimeField(default=datetime.now,auto_now=False)

class Receipt(models.Model):
    receipt_date=models.DateTimeField(default=datetime.now,auto_now=False)
    receipt_description=models.TextField
    name=models.CharField(max_length=12)
    balance=models.BigIntegerField
    amount=models.BigIntegerField
    file=models.FileField

class Loan(models.Model):
    loan_id=models.IntegerField
    loan_type=models.CharField
    amount=models.IntegerField
    loan_status=models.CharField
    name=models.CharField
    purpose_of_the_loan=models.CharField
    Wallet=models.OneToOneField
    date_issued=models.DateTimeField(default=datetime.now,auto_now=False)
    payment_due_date=models.DateTimeField(default=datetime.now)
    loan_balance=models.IntegerField
    interest_rate=models.SmallIntegerField
    guarantor=models.ForeignKey
    
class Reward(models.Model):
    date_of_reward=models.DateTimeField(default=datetime.now)
    description_of_reward=models.TextField
    reward_points=models.SmallIntegerField
    Wallet=models.ForeignKey











