import form
from .models import Order
from django import forms
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'username')

