from django import forms
from .models import Account

class TransferForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver'].queryset = Account.objects.all().exclude(pk=user.pk)
        
    receiver = forms.ModelChoiceField(queryset=Account.objects.none())
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
