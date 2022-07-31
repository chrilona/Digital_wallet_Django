from django.contrib import admin
from .models import Account, Customer, Notification, Receipt,Transaction, Wallet,Card,Thirdparty,Notification,Receipt,Loan,Reward

class CustomerAdmin(admin.ModelAdmin):
    list_display= ("firstname","lastname","address",)
    search_fields= ("firstname","lastname",)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Transaction)


# Register your models here.
