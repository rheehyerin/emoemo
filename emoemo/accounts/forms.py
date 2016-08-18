from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    username = forms.EmailField(label='Email')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user