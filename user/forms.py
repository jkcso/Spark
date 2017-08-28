from django import forms
from django.contrib.auth.models import User


# Used for user sign up
class UserForm(forms.ModelForm):
    # to make password not visible, having the bullet points.
    password = forms.CharField(widget=forms.PasswordInput)

    # info about our class
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
