from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, ClearableFileInput, NumberInput, EmailInput

from .models import GraphiCards
# from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserRegistrationModel
from django.contrib.auth.forms import PasswordResetForm


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')




class GraphicForm(forms.ModelForm):
    class Meta:
        model = GraphiCards
        fields = ('name','Reference', 'image','Quantity','price', )
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'name'
                }),
            'Reference': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'file_name'
                }),
            'image': ClearableFileInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'file path'
            }),
            'Quantity': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Quantity'
            }),
            'price': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'price'
            })
        }

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        fields = ('from_email', 'subject', 'message',)
        widgets = {
            'from_email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'name'
                }),
            'subject': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'file_name'
                }),
            'image': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'file path'
            })
        }

