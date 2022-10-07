from django.urls import path,include
from .views import CustomerViewset,AccountViewset,WalletViewset,CardViewset,LoanViewset,ThirdpartyViewset,NotificationViewset,RewardViewset,ReceiptViewset
from rest_framework import routers

router =routers.DefaultRouter()
router.register (r"customers", CustomerViewset)
router.register (r"accounts", AccountViewset)
router.register (r"wallets", WalletViewset)
router.register (r"cards", CardViewset)
router.register (r"loans", LoanViewset)
router.register (r"thirdpartys", ThirdpartyViewset)
router.register (r"notifications", NotificationViewset)
router.register (r"rewards", RewardViewset)
router.register (r"receipts", ReceiptViewset)



urlpatterns=[
 path("",include(router.urls)),

]