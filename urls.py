from django.urls import path
from .views import CreateAccount, ClientCreateAccount, AccountList, TransactionCreate , TransactionList

urlpatterns = [
	path('create/', CreateAccount.as_view(), name='create-account'),
	path('client/create/', ClientCreateAccount.as_view(), name='client-create-account'),
	path('list/', AccountList.as_view(), name='list-account'),
	path('transaction/',TransactionCreate.as_view(),name='transaction-create'),
	path('transaction_list/',TransactionList.as_view(),name='transaction-list'),
]