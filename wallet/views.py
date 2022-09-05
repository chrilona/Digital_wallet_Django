from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdpartyRegistrationForm, TransactionRegistrationForm,WalletRegistrationForm

def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html" ,{"form":form})

def register_wallet(request):
    wallett = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html" ,{"form":wallett})

def register_account(request):
    account = AccountRegistrationForm()
    return render(request,"wallet/register_account.html" ,{"form":account})

def register_receipt(request):
    receipt = ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html" ,{"form":receipt})

def register_transaction(request):
    transaction = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html" ,{"form":transaction})

def register_card(request):
    card = CardRegistrationForm()
    return render(request,"wallet/register_card.html" ,{"form":card})

def register_thirdparty(request):
    thirdparty = ThirdpartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html" ,{"form":thirdparty})

def register_notification(request):
    note = NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html" ,{"form":note})

def register_loan(request):
    loan = LoanRegistrationForm()
    return render(request,"wallet/register_loan.html" ,{"form":loan})

def register_reward(request):
    reward = RewardRegistrationForm()
    return render(request,"wallet/register_reward.html" ,{"form":reward})

# Create your views here.
