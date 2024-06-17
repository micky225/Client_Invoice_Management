from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['recipient','description','num_items','expiration_date']

        widgets = {
            'recipient': forms.TextInput(attrs={
                'class': 'outline-none text-sm rounded-lg block w-full p-2.5 bg-gray-100 placeholder-gray-600',
                'placeholder': 'recipient',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'outline-none text-sm rounded-lg block w-full p-2.5 bg-gray-100 placeholder-gray-600',
            }),
            'num_items': forms.NumberInput(attrs={
                'class': 'outline-none text-sm rounded-lg block w-full p-2.5 bg-gray-100 placeholder-gray-600',
                'placeholder': '123 ...',
                'required': True,
            }),
            'expiration_date': forms.DateInput(attrs={
                'class': 'outline-none text-sm rounded-lg block w-full p-2.5 bg-gray-100 placeholder-gray-600',
                'placeholder': 'yyyy-mm-dd',
                'required': True,
            }),
        }
        