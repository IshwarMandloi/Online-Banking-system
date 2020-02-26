from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, View, ListView
from .models import AccountDetails, Transaction

# Create your views here.
class CreateAccount(CreateView):
	model = AccountDetails
	fields = ['account_no', 'account_type', 'ifsc_code', 'client']
	success_url = '/accounts/list/'

class ClientCreateAccount(CreateView):
	model = AccountDetails
	fields = ['account_no', 'account_type', 'ifsc_code']
	success_url = '/accounts/list/'

	def form_valid(self, form):
		form.instance.client = self.request.user
		return super(ClientCreateAccount, self).form_valid(form)

class AccountList(ListView):
	model = AccountDetails

	def get_queryset(self):
		if self.request.user.is_superuser:
			return super(AccountList, self).get_queryset()
		else:
			return self.model.objects.filter(client=self.request.user)

class TransactionCreate(CreateView):
	model=Transaction
	fields=['account','amount','transaction_type','transaction_medium']
	success_url='/account/list/'

class TransactionList(ListView):
	model = Transaction
