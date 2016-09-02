from django import forms
from django.contrib.auth.models import User
from .models import Emp


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = [
            "firstName",
            "lastName",
            "email",
            "sex"
        ]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]