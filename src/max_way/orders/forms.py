from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['address']
        widgets = {
            "address" : forms.TextInput(attrs= {
                "class": "text", "placeholder": "Enter your address", "cols":"30","rows":"10"
            })
        }