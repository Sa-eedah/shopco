from django import forms
# Import Django forms module
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Import Django's built-in forms for user creation and authentication
from django.contrib.auth.models import User
# Import Django's default User model
from .models import Review

class LoginForm(AuthenticationForm):
    # Custom login form that extends Django's built-in AuthenticationForm
    # Username field with custom styling
    username = forms.CharField(widget=forms.TextInput (attrs={
        'placeholder':'Your username', # Hint text shown in the field
        'class': 'form-group',
    }))
     # Password field with custom styling and placeholder text
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class': 'form-group',
    }))

    # Custom signup form that extends Django's built-in UserCreationForm
class SignupForm(UserCreationForm):
     # Meta class defines which model and fields to use for this form   
    class Meta:
        model = User   # Use Django's built-in User model
        fields = ('username','email','password1','password2') # Fields to include in form

    username = forms.CharField(widget=forms.TextInput (attrs={
        'placeholder':'Your username', # Hint text for username
        'class': 'form-group', # CSS styling classes
    }))

    email = forms.CharField(widget=forms.EmailInput (attrs={
        'placeholder':'Your email address', # Hint text for email
        'class': 'form-group', # CSS styling classes
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password', # Hint text for password
        'class': 'form-group', # CSS styling classes
    }))

    password2 = forms.CharField(widget=forms.PasswordInput (attrs={
        'placeholder':'Repeat Password', # Hint text for password2
        'class': 'form-group',# CSS styling classes
    }))
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'input-field'}),
            'text': forms.Textarea(attrs={'placeholder': 'Write your review...', 'class': 'textarea-field'}),
        }

