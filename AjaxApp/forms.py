from dataclasses import field
import email
from pyexpat import model
from django import forms
from .models import person

class PersonRegistration(forms.ModelForm):
    class Meta:
        model = person
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'})
        }