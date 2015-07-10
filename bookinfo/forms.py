from django import forms

from bookinfo.models import AddressBook


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = AddressBook
        fields = ['contact_address','name','mobile']

    

