from django import forms

class LogIn(forms.Form):
    user_name= forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder': 'username or password'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'password' }))


class CreateAccountForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    re_password = forms.CharField()
