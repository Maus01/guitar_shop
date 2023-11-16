from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
    
    user_name = forms.CharField(
        label='Username', min_length=4, max_length=50, help_text='Required'
    )
    email = forms.EmailField(label="E-mail", max_length=100, help_text='Required', error_messages={'required':'E-mail required'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Validation', widget=forms.PasswordInput)
    
    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)
        
    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Passwords do not match!!')
        return data['password2']
    
class LoginForm(AuthenticationForm):   
    username = forms.CharField(label='E-mail', max_length=150, widget=forms.TextInput, error_messages={'required': 'E-mail is required'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=150, error_messages={'required': 'Password is required'})
    
   
    
    
   