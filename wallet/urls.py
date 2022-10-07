from django.urls import path 
from .views import account_profile, card_profile, customer_profile, edit_account, edit_card, edit_profile, edit_receipt, edit_transaction, edit_wallet, list_accounts, list_cards, list_loans, list_notifications, list_receipts, list_rewards, list_thirdpartys, list_transactions, list_wallets, receipt_profile, register_account, register_customer,register_card, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet,list_customers, transaction_profile, wallet_profile,list_loans

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
    path("thirdpartys/",list_thirdpartys,name="thirdpartys"),  
    path("notifications/",list_notifications,name="notifications_list"),  
    path("loans/",list_loans,name="list_loans"),
    path("rewards/",list_rewards,name="rewards_list"),
    
    path("customers/<int:id>/",customer_profile,name="customer_profile"),
    path("customers/edit/<int:id>/",edit_profile,name="edit_profile"),

    path("wallets/<int:id>/",wallet_profile,name="wallet_profile"),
    path("wallets/edit/<int:id>/",edit_wallet,name="edit_wallet"),
    
    path("accounts/<int:id>/",account_profile,name="account_profile"),
    path("accounts/edit/<int:id>/",edit_account,name="edit_account"),
    
    path("cards/<int:id>/",card_profile,name="card_profile"),
    path("cards/edit/<int:id>/",edit_card,name="edit_card"),
    
    path("transactions/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transactions/edit/<int:id>/",edit_transaction,name="edit_transaction"),

    path("receipts/<int:id>/",receipt_profile,name="receipt_profile"),
    path("receipts/edit/<int:id>/",edit_receipt,name="edit_receipt"),
    
    ]