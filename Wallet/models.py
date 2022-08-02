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
    gender_choices=(
        ("M" ,"Male"),
        ("F","Female")
    )
    gender=models.CharField(max_length=1,choices=gender_choices,null=True)
    profile_picture=models.ImageField

    # def __str__(self):
    #     return self.firstname
        
class Wallet(models.Model):
    balance=models.BigIntegerField(default=0)
    isactive=models.BooleanField(max_length=1,null=True)
    Customer=models.OneToOneField
    pin=models.PositiveSmallIntegerField
    currency=models.CharField(max_length=8)
    date_created=models.DateTimeField(default=datetime.now)

class Account(models.Model):
    account_number = models.IntegerField()
    account_name=models.CharField(max_length=14)
    account_type=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=8,null=True)
    balance=models.IntegerField
    wallet=models.ForeignObject

class Transaction(models.Model):
    transaction_code = models.IntegerField
    transaction_amount = models.BigIntegerField
    transaction_charges = models.IntegerField(null=True)
    transaction_date_time = models.DateTimeField(default=datetime.now)
    origin_account = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="Account_a")
    destination_account = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="Account_b")
    Receipt = models.OneToOneField

class Card(models.Model):
    serial_number =models.IntegerField(null=True)
    date_issued = models.DateTimeField(default=datetime.now,auto_now=False)
    expiry_date=models.DateTimeField(default=datetime.now,auto_now=False)
    signature=models.ImageField
    Account=models.ForeignKey(on_delete=models.CASCADE,to=Account,null=True)
    Wallet=models.ForeignKey(on_delete=models.CASCADE,to=Wallet,null=True)
    issuer=models.CharField

class Thirdparty(models.Model):
    name=models.CharField(max_length=18,null=True)
    currency=models.ForeignKey
    transaction_cost=models.IntegerField
    Account=models.OneToOneField(on_delete=models.CASCADE,to=Account,null=True)

class Notification(models.Model):
    description=models.TextField
    title=models.CharField(max_length=8)
    recipient=models.ForeignKey(on_delete=models.CASCADE,to=Customer,null=True)
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
    loan_type=models.CharField(max_length=28,null=True)
    amount=models.IntegerField(null=True)
    loan_status=models.CharField
    name=models.CharField
    purpose_of_the_loan=models.CharField
    Wallet=models.OneToOneField(on_delete=models.CASCADE,to=Wallet,default=0)
    date_issued=models.DateTimeField(default=datetime.now,auto_now=False)
    payment_due_date=models.DateTimeField(default=datetime.now)
    loan_balance=models.IntegerField(null=True)
    interest_rate=models.SmallIntegerField
    guarantor=models.ForeignObject
    
class Reward(models.Model):
    date_of_reward=models.DateTimeField(default=datetime.now)
    description_of_reward=models.TextField
    reward_points=models.SmallIntegerField(null=True)
    Wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True)











