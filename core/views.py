from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Account, Transaction
from .forms import TransferForm

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    return render(request, 'banking/home.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    accounts = customer.accounts.all()
    return render(request, 'banking/customer_detail.html', {'customer': customer, 'accounts': accounts})

def account_detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    sent_transactions = account.sent_transactions.all()
    received_transactions = account.received_transactions.all()
    return render(request, 'banking/account_detail.html', {'account': account, 'sent_transactions': sent_transactions, 'received_transactions': received_transactions})

def transfer(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']
            if account.account_balance >= amount:
                account.account_balance -= amount
                account.save()
                receiver.account_balance += amount
                receiver.save()
                Transaction.objects.create(sender=account, receiver=receiver, amount=amount)
                return redirect('account_detail', account_id=account.id)
    else:
        form = TransferForm()
    return render(request, 'banking/transfer.html', {'form': form, 'account': account})