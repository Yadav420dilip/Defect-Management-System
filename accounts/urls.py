from django.urls import path
from accounts.views import Account_Login, acc_logout

urlpatterns = [
    path('login/', Account_Login.as_view(), name='login'),
    path('logout/', acc_logout, name='logout'),
]
