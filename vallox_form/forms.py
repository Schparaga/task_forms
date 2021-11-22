from .models import Customer
#from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, CharField


class TechnicalTask(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_surname','customer_phone', 'customer_email', 'category', 'body']

        widgets = {
            "customer_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Customer name'
             }),
            "customer_surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Customer surname'
             }),
        }

#    customer_name = forms.CharField(label='First and second name', max_length=100)
#    customer_phone = forms.IntegerField()
#    customer_email = forms.EmailField(label='E-mail')
#    category = forms.ChoiceField(choices=[('cottege', 'Cottage'), ('apartment', 'Apartment')])
#    body = forms.CharField(widget=forms.Textarea)
