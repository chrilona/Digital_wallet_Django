from django.shortcuts import redirect, render
from . import forms
from. import models
import wallet

def register_customer(request):
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html" ,{"form":form})

def list_customers(request):
    customer = models.Customer.objects.all()
    return render(request,'wallet/customer_list.html',{"customer":customer})

def register_wallet(request):
    if request.method == "POST":
       form = forms.WalletRegistrationForm(request.POST)
       if form.is_valid():
            form.save()
    else:
        form=forms.CustomerRegistrationForm()       
    return render(request,"wallet/register_wallet.html" ,{"form":form})

def list_wallets(request):
    wallet = models.Wallet.objects.all()
    return render(request,'wallet/wallet_list.html',{"Wallet":wallet})

def register_account(request):
    if request.method == "POST":
     form = forms.AccountRegistrationForm(request.POST)
     if form.is_valid():
            form.save()
    else:
        form=forms.AccountRegistrationForm() 
    return render(request,"wallet/register_account.html" ,{"form":form})

def list_accounts(request):
    account = models.Account.objects.all()
    return render(request,'wallet/account_list.html',{"Account":account})

def register_receipt(request):
    if request.method == "POST":
     form = forms.ReceiptRegistrationForm(request.POST)
     if form.is_valid():
            form.save() 
    else:
        form=forms.ReceiptRegistrationForm()  
    return render(request,"wallet/register_receipt.html" ,{"form":form})

def list_receipts(request):
    receipts = models.Receipt.objects.all()
    return render(request,'wallet/receipt_list.html',{"receipts":receipts})


def register_transaction(request):
    if request.method == "POST":
     form = forms.TransactionRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=forms.TransactionRegistrationForm()  
    return render(request,"wallet/register_transaction.html" ,{"form":form})

def list_transactions(request):
    transaction = models.Transaction.objects.all()
    return render(request,'wallet/transcation_list.html',{"Transaction":transaction})

def register_card(request):
    if request.method == "POST":
     form = forms.CardRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=forms.CardRegistrationForm()  
    return render(request,"wallet/register_card.html" ,{"form":form})

def list_cards(request):
    card = models.Card.objects.all()
    return render(request,'wallet/card_list.html',{"Card":card})

def register_thirdparty(request):
    if request.method == "POST":
     form = forms.ThirdpartyRegistrationForm()
     if form.is_valid():
            form.save()

    else:
        form=forms.ThirdpartyRegistrationForm()  
    return render(request,"wallet/register_thirdparty.html" ,{"form":form})

def list_thirdpartys(request):
    thirdparty = models.Thirdparty.objects.all()
    return render(request,'wallet/thirdparty_list.html',{"thirdparty":thirdparty})

def register_notification(request):
    if request.method == "POST":
     form = forms.NotificationRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=forms.NotificationRegistrationForm()  
    return render(request,"wallet/register_notification.html" ,{"form":form})

def list_notifications(request):
    notification = models.Notification.objects.all()
    return render(request,'wallet/notification_list.html',{"Notification":notification})

def register_loan(request):
    if request.method == "POST":
     form = forms.LoanRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=forms.LoanRegistrationForm()  
    return render(request,"wallet/register_loan.html" ,{"form":form})

def list_loans(request):
    loan = models.Loan.objects.all()
    return render(request,'wallet/loan_list.html',{"Loan":loan})

def register_reward(request):
    if request.method == "POST":
     form = forms.RewardRegistrationForm()
     if form.is_valid():
            form.save()
    else:
        form=forms.RewardRegistrationForm()  
    return render(request,"wallet/register_reward.html" ,{"form":form})

def list_rewards(request):
    rewards = models.Reward.objects.all()
    return render(request,'wallet/reward_list.html',{"rewards":rewards})

def customer_profile(request ,id):
    customer = models.Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",
    {"customer":customer})

def edit_profile(request,id):
    customer=models.Customer.objects.get(id=id)
    if request.method =="POST":
        form=forms.CustomerRegistrationForm(request.POST,instance=models.Customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customer.id)
    else:
        form=forms.CustomerRegistrationForm(instance=models.Customer)
        return render(request,"wallet/edit_profile.html",{"form":form})
# Create your views here.

def wallet_profile(request,id):
    wallet = models.Wallet.objects.get(id=id)
    return render(request, 'wallet/wallet_profile.html',{'wallet': wallet})

def edit_wallet(request,id):
    wallet=models.Wallet.objects.get(id=id)
    if request.method =="POST":
        form=forms.WalletRegistrationForm(request.POST,instance=models.Wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile",id=wallet.id)
    else:
        form=forms.WalletRegistrationForm(instance=models.Wallet)
        return render(request,"wallet/edit_wallet.html",{"form":form})

def account_profile(request,id):
    account = models.Account.objects.get(id=id)
    return render(request, 'wallet/account_profile.html',{'account': account})

def edit_account(request,id):
    account=models.Account.objects.get(id=id)
    if request.method =="POST":
        form=forms.AccountRegistrationForm(request.POST,instance=models.Account)
        if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
        form=forms.AccountRegistrationForm(instance=models.Account)
        return render(request,"wallet/edit_account.html",{"form":form})

def card_profile(request,id):
    card = models.Card.objects.get(id=id)
    return render(request, 'wallet/card_profile.html',{'card': card})

def edit_card(request,id):
    card=models.Card.objects.get(id=id)
    if request.method =="POST":
        form=forms.CardRegistrationForm(request.POST,instance=models.Card)
        if form.is_valid():
            form.save()
            return redirect("card_profile",id=card.id)
    else:
        form=forms.CardRegistrationForm(instance=models.Card)
        return render(request,"wallet/edit_card.html",{"form":form})

def receipt_profile(request,id):
    receipt = models.Receipt.objects.get(id=id)
    return render(request, 'wallet/receipt_profile.html',{'receipt': receipt})

def edit_receipt(request,id):
    card=models.Receipt.objects.get(id=id)
    if request.method =="POST":
        form=forms.ReceiptRegistrationForm(request.POST,instance=models.Receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=card.id)
    else:
        form=forms.CardRegistrationForm(instance=models.Receipt)
        return render(request,"wallet/edit_receipt.html",{"form":form})

def transaction_profile(request,id):
    transaction = models.Transaction.objects.get(id=id)
    return render(request, 'wallet/transaction_profile.html',{'transaction': transaction})

def edit_transaction(request,id):
    transaction=models.Transaction.objects.get(id=id)
    if request.method =="POST":
        form=forms.TransactionRegistrationForm(request.POST,instance=models.Transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)
    else:
        form=forms.TransactionRegistrationForm(instance=models.Transaction)
        return render(request,"wallet/edit_transaction.html",{"form":form})

