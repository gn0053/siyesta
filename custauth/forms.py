from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=60, error_messages={'required': 'Username is required'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Password is required'})