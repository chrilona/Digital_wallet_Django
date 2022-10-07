from curses import meta
from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Wallet 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields=("firstname","emails","lastname")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields=("account_number","account_name","account_type","password","balance","wallet")

class  WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields=("isactive","balance","customer","pin","currency","date_created")

class  ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model= Receipt
        fields=("receipt_date","receipt_description","name","balance","amount","file")

class  CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields=("serial_number","date_issued","expiry_date","signature","account","wallet","issuer")   


class  ThirdpartySerializer(serializers.ModelSerializer):
    class Meta:
        model= Thirdparty
        fields=("name","currency","transaction_cost","account")             

class  NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields=("description","title","recipient","read_unread_status","date_and_time")      

class  LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields=("loan_id","loan_type","amount","loan_status","name","purpose_of_the_loan","wallet","date_issued","payment_due_date","loan_balance","interest_rate","guarantor")       

class  RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reward
        fields=("date_of_reward","description_of_reward","reward_points","wallet")               