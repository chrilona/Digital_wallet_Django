from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer,AccountSerializer,WalletSerializer,ReceiptSerializer,CardSerializer,ThirdpartySerializer,NotificationSerializer,LoanSerializer,RewardSerializer
from wallet.models import Customer,Account, Notification,Wallet,Receipt,Card,Thirdparty,Loan,Reward

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class=CustomerSerializer

class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class=AccountSerializer

class WalletViewset(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class=WalletSerializer

class ReceiptViewset(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class=ReceiptSerializer

class CardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class=CardSerializer

class ThirdpartyViewset(viewsets.ModelViewSet):
    queryset = Thirdparty.objects.all()
    serializer_class=ThirdpartySerializer

class NotificationViewset(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class=NotificationSerializer


class LoanViewset(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class=LoanSerializer

class RewardViewset(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class=RewardSerializer
# Create your views here.
