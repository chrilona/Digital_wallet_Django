from django.shortcuts import render

from wallet.models import Customer
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdpartyRegistrationForm, TransactionRegistrationForm,WalletRegistrationForm
from.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet
def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html" ,{"form":form})

def list_customers(request):
    customer = Customer.objects.all()
    return render(request,'wallet/customer_list.html',{"Customer":customer})

def register_wallet(request):
    if request.method == "POST":
       form = WalletRegistrationForm(request.POST)
       if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()       
    return render(request,"wallet/register_wallet.html" ,{"form":form})

def list_wallets(request):
    wallet = Wallet.objects.all()
    return render(request,'wallet/wallet_list.html',{"Wallet":wallet})

def register_account(request):
    if request.method == "POST":
     form = AccountRegistrationForm(request.POST)
     if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm() 
    return render(request,"wallet/register_account.html" ,{"form":form})

def list_accounts(request):
    account = Account.objects.all()
    return render(request,'wallet/account_list.html',{"Account":account})

def register_receipt(request):
    if request.method == "POST":
     form = ReceiptRegistrationForm(request.POST)
     if form.is_valid():
            form.save() 
    else:
        form=ReceiptRegistrationForm()  
    return render(request,"wallet/register_receipt.html" ,{"form":form})

def list_receipts(request):
    receipt = Receipt.objects.all()
    return render(request,'wallet/receipt_list.html',{"Receipt":receipt})


def register_transaction(request):
    if request.method == "POST":
     form = TransactionRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm()  
    return render(request,"wallet/register_transaction.html" ,{"form":form})

def list_transactions(request):
    transaction = Transaction.objects.all()
    return render(request,'wallet/transcation_list.html',{"Transaction":transaction})

def register_card(request):
    if request.method == "POST":
     form = CardRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()  
    return render(request,"wallet/register_card.html" ,{"form":form})

def list_cards(request):
    card = Card.objects.all()
    return render(request,'wallet/card_list.html',{"Card":card})

def register_thirdparty(request):
    if request.method == "POST":
     form = ThirdpartyRegistrationForm()
     if form.is_valid():
            form.save()

    else:
        form=ThirdpartyRegistrationForm()  
    return render(request,"wallet/register_thirdparty.html" ,{"form":form})

def list_thirdpartys(request):
    thirdparty = Thirdparty.objects.all()
    return render(request,'wallet/thirdparty_list.html',{"Thirdparty":thirdparty})

def register_notification(request):
    if request.method == "POST":
     form = NotificationRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=NotificationRegistrationForm()  
    return render(request,"wallet/register_notification.html" ,{"form":form})

def list_notifications(request):
    notification = Notification.objects.all()
    return render(request,'wallet/notification_list.html',{"Notification":notification})

def register_loan(request):
    if request.method == "POST":
     form = LoanRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm()  
    return render(request,"wallet/register_loan.html" ,{"form":form})

def list_loans(request):
    loan = Loan.objects.all()
    return render(request,'wallet/loan_list.html',{"Loan":loan})

def register_reward(request):
    if request.method == "POST":
     form = RewardRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm()  
    return render(request,"wallet/register_reward.html" ,{"form":form})

def list_rewards(request):
    reward = Reward.objects.all()
    return render(request,'wallet/reward_list.html',{"Reward":reward})

# Create your views here.
