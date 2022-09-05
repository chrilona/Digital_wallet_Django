
from django.db import models
from django.utils import timezone

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
    profile_picture=models.ImageField(upload_to='profile_picture/')

    # def __str__(self):
    #     return self.firstname
        
class Wallet(models.Model):
    isactive=models.BooleanField(max_length=1,null=True)
    balance=models.BigIntegerField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Wallet_customer')
    pin=models.PositiveSmallIntegerField()
    currency=models.CharField(max_length=8,null=True)
    date_created=models.DateField(default=timezone.now)

class Account(models.Model):
    account_number = models.IntegerField()
    account_name=models.CharField(max_length=14,null=True)
    account_type=models.CharField(max_length=14,null=True)
    password=models.CharField(max_length=8,null=True)
    balance=models.IntegerField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Account_wallet')

class Receipt(models.Model):
    receipt_date=models.DateField(default=timezone.now)
    receipt_description=models.TextField()
    name=models.CharField(max_length=12,null=True)
    balance=models.BigIntegerField()
    amount=models.BigIntegerField()
    file=models.FileField(upload_to='Wallet/')    

class Transaction(models.Model):
    transaction_code = models.IntegerField()
    transaction_amount = models.BigIntegerField()
    transaction_charges = models.IntegerField()
    transaction_date_time = models.DateField(default=timezone.now)
    origin_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_origin_account')
    destination_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_destination_account')
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,related_name='Transaction_receipt')

class Card(models.Model):
    serial_number =models.IntegerField()
    date_issued = models.DateField(default=timezone.now)
    expiry_date=models.DateField(default=timezone.now)
    signature =models.ImageField(upload_to='signature')
    account =models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Card_wallet')
    wallet =models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Card_wallet')
    issuer =models.CharField(max_length=20,null=True)

class Thirdparty(models.Model):
    name=models.CharField(max_length=18,null=True)
    currency=models.CharField(max_length=200,null=True)
    transaction_cost=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='Thirdparty_transaction')
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Thirdparty_account')

class Notification(models.Model):
    description=models.TextField()
    title=models.CharField(max_length=20,null=True)
    recipient=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Notification_recipient')
    read_unread_status =models.CharField(max_length=20,null=True)
    date_and_time =models.DateField(default=timezone.now)

class Loan(models.Model):
    loan_id=models.IntegerField()
    loan_type =models.CharField(max_length=28,null=True)
    amount=models.IntegerField()
    loan_status =models.CharField(max_length=20,null=True)
    name=models.CharField(max_length=50,null=True)
    purpose_of_the_loan =models.CharField(max_length=200,null=True)
    wallet =models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Loan_wallet')
    date_issued =models.DateField(default=timezone.now)
    payment_due_date =models.DateField(default=timezone.now)
    loan_balance =models.IntegerField()
    interest_rate =models.SmallIntegerField()
    guarantor =models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Loan_customer')
    
class Reward(models.Model):
    date_of_reward=models.DateTimeField(default=timezone.now)
    description_of_reward =models.TextField()
    reward_points =models.SmallIntegerField()
    wallet =models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Reward_wallet')











