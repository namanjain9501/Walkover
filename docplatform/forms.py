from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms
from django.forms import ModelForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter firstname"

            }
        )
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter Lastname"
            }
        )
    )
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "Enter Email-id"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Enter Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Re-enter Password"
    }))
    

    

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class Uploadform(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ('doc_name','doc')

class Createform(forms.ModelForm):
    class Meta:
        model = Workspace
        fields = ['name','desc']
