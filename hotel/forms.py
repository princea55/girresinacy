from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ContactUs
from django.contrib.auth.forms import PasswordResetForm 

class SignupUser(UserCreationForm):
    contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contact'}), min_length=10, max_length=10, label='')
    email = forms.EmailField(max_length=40, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}), help_text="Enter right email to activate your account")
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'autofocus': 'autofocus'}))
    last_name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(max_length=200, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=200, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}))
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2','contact']


class LoginUser(forms.Form):
    username=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Username or Email Address', 'autofocus': 'autofocus'}))
    password=forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ConatctUsForm(forms.ModelForm):
    fullName = forms.CharField(max_length=20, required="This Field is required" ,label='', widget=forms.TextInput(attrs={'placeholder': 'FullName'}))
    email = forms.EmailField(max_length=40, required="This Field is required" , label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(max_length=200, required="This Field is required",  label='', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Write your message here...'}))
    class Meta:
        model = ContactUs
        fields= ['fullName','email','subject','message']

class Passwordresetform(PasswordResetForm):
    email = forms.EmailField(max_length=40, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}), help_text="Enter right email to reset Your password")

class ConfirmPasswordresetform(forms.Form):
    password1 = forms.CharField(max_length=200, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=200, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}))

