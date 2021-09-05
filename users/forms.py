from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
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
        self.fields['first_name'].required = True

        self.fields['last_name'].error_messages={'required': 'Campo obrigatório'}
        self.fields['last_name'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['last_name'].required = True

        self.fields['password1'].error_messages={'required': 'Campo obrigatório'}
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['password2'].error_messages={'required': 'Campo obrigatório'}
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['cpf'].error_messages={'required': 'Campo obrigatório'}
        self.fields['cpf'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })
        self.fields['cpf'].required = True

        self.fields['cellphone'].error_messages={'required': 'Campo obrigatório'}
        self.fields['cellphone'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })
        self.fields['cellphone'].required = True

        self.fields['address'].error_messages={'required': 'Campo obrigatório'}
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['address'].required = True
    
    def clean_cellphone(self):
        data = self.cleaned_data['cellphone']
        if not data.isdigit():
            raise ValidationError("Por favor insira somente números")

        return data
    
    def clean_cpf(self):
        data = self.cleaned_data['cpf']
        if not data.isdigit():
            raise ValidationError("Por favor insira somente números")

        if len(data) < 11:
            raise ValidationError("Cpf não é válido")
        
        if data in [s * 11 for s in [str(n) for n in range(10)]]:
            raise ValidationError("Cpf não é válido")
        
        calc = lambda t: int(t[1]) * (t[0] + 2)
        d1 = (sum(map(calc, enumerate(reversed(data[:-2])))) * 10) % 11
        d2 = (sum(map(calc, enumerate(reversed(data[:-1])))) * 10) % 11
        if str(d1) == data[-2] and str(d2) == data[-1]:
            return data
        else:
            raise ValidationError("Cpf não é válido")

class UserLoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': 'Campo obrigatório.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )

    password = forms.CharField(
        error_messages={'required': 'Campo obrigatório.'},
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'})
    )