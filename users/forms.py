from django.contrib.auth import forms as auth_forms
from django import forms

from users.models import User


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'cpf', 'cellphone', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].error_messages={'required': 'Campo obrigatório'}
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['email'].error_messages={'required': 'Campo obrigatório.'}
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['first_name'].error_messages={'required': 'Campo obrigatório'}
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['last_name'].error_messages={'required': 'Campo obrigatório'}
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['password1'].error_messages={'required': 'Campo obrigatório'}
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['password2'].error_messages={'required': 'Campo obrigatório'}
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['cpf'].error_messages={'required': 'Campo obrigatório'}
        self.fields['cpf'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['cellphone'].error_messages={'required': 'Campo obrigatório'}
        self.fields['cellphone'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['address'].error_messages={'required': 'Campo obrigatório'}
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-sm'})

class UserLoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': 'Campo obrigatório.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )

    password = forms.CharField(
        error_messages={'required': 'Campo obrigatório.'},
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'})
    )