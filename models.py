from django.db import models
from users.models import CustomUser
from django.db.models import Avg, Count, Min, Sum

ACCOUNT_TYPE = ((1, 'Saving'), (2, 'Current'))
TRANSACTION_TYPE = ((1, 'Withdraw'), (2, 'Deposit'))
TRANSACTION_MEDIUM = ((1, 'Cheque'), (2, 'Cash'), (3, 'NEFT'))
# Create your models here.
class AccountDetails(models.Model):
	account_no = models.CharField(max_length=30)
	ifsc_code = models.CharField(max_length=30)
	account_type = models.IntegerField(choices=ACCOUNT_TYPE)
	client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	def __str__(self):
		return "%s || %s"%(self.account_no, self.get_account_type_display())

	def get_all_withdrawl_transactions(self):
		return self.transactions.filter(transaction_type=1)

	def get_all_deposit_transactions(self):
		return self.transactions.filter(transaction_type=2)

class Transaction(models.Model):
	account = models.ForeignKey(AccountDetails, on_delete=models.CASCADE, related_name='transactions')
	amount = models.IntegerField()
	transaction_type = models.IntegerField(choices=TRANSACTION_TYPE)
	transaction_medium = models.IntegerField(choices=TRANSACTION_MEDIUM)
	created_at = models.DateTimeField(auto_now_add=True)
