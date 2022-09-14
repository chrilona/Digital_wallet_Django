from django.urls import path 
from .views import list_accounts, list_cards, list_loans, list_notifications, list_receipts, list_rewards, list_thirdpartys, list_transactions, list_wallets, register_account, register_customer,register_card, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet,list_customers

urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="wallet"),
    path("account/",register_account,name="account"),
    path("receipt/",register_receipt,name="receipt"),
    path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("notification/",register_notification,name="notification"),
    path("loan/",register_loan,name="loan"),
    path("reward/",register_reward,name="reward"),
    path("customers/",list_customers,name="customers_list"),
    path("wallets/",list_wallets,name="wallets_list"),
    path("accounts/",list_accounts,name="accounts_list"),
    path("receipts/",list_receipts,name="receipts_list"),
    path("transactions/",list_transactions,name="transactions_list"),
    path("cards/",list_cards,name="cards_list"),
    path("thirdpartys/",list_thirdpartys,name="thirdpartys_list"),  
    path("notifications/",list_notifications,name="notifications_list"),  
    path("loans/",list_loans,name="loans_list"),
    path("rewards/",list_rewards,name="rewards_list"),
    ]