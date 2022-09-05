from django.contrib import admin
from .models import Account, Customer, Receipt,Transaction, Wallet,Card,Thirdparty,Notification,Loan,Reward

class CustomerAdmin(admin.ModelAdmin):
    list_display= ("firstname","lastname","address",)
    search_fields= ("firstname","lastname",)

admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display= ("isactive" ,"balance" ,"customer", "pin","currency" ,"date_created")
    search_fields= ("balance","currency","date_created")

admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display= ("account_number","account_name","account_type","password","balance","wallet")
    search_fields= ("account_number","account_name","account_type","password","balance","wallet")

admin.site.register(Account,AccountAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display= ("receipt_date","receipt_description","name","balance","amount","file")
    search_fields= ("receipt_date","receipt_description","name","balance","amount","file")

admin.site.register(Receipt,ReceiptAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display= ("transaction_code","transaction_amount","transaction_charges","origin_account","destination_account","receipt")
    search_fields= ("transaction_code","transaction_amount","transaction_charges","origin_account","destination_account","receipt")

admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display= ("serial_number","date_issued","expiry_date","signature","account","wallet","issuer")
    search_fields= ("serial_number","date_issued","expiry_date","signature","account","wallet","issuer")

admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display= ("name","currency","transaction_cost")
    search_fields= ("name","currency","transaction_cost")

admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display= ("description","title","recipient","read_unread_status","date_and_time")
    search_fields= ("description","title","recipient","read_unread_status","date_and_time")

admin.site.register(Notification,NotificationAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display= ("loan_id","loan_type","amount","loan_status","name","purpose_of_the_loan","wallet","date_issued","payment_due_date","loan_balance" , "interest_rate")
    search_fields= ("loan_id","loan_type","amount","loan_status","name","purpose_of_the_loan","wallet","date_issued","payment_due_date","loan_balance "," interest_rate")

admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display= ("date_of_reward","description_of_reward","reward_points","wallet")
    search_fields= ("date_of_reward","description_of_reward","reward_points","wallet")

admin.site.register(Reward,RewardAdmin)
# Register your models here.
