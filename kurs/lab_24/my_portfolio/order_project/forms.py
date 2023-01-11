from django.forms import ModelForm, TextInput, Select, Textarea

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name_customer', 'phone_customer', 'email_customer', 'title', 'body', 'type_website']
        widgets = {
            'name_customer': TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            'phone_customer': TextInput(attrs={"class": "form-control", "placeholder": "Your Phone"}),
            'email_customer': TextInput(attrs={"class": "form-control", "placeholder": "Your Email"}),
            'title': TextInput(attrs={"class": "form-control", "placeholder": "Your Project Name"}),
            'body': Textarea(attrs={"class": "form-control", "placeholder": "Describe Your Project"}),
            'type_website': Select(attrs={"class": "form-control"}),
        }
