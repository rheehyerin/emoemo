from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Follow

class SignupForm(UserCreationForm):

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class FollowModelForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ['to_user']
        labels = {
            'to_user': '추가할 친구 ID',
        }

class UserIdForm(forms.Form):
    user_id = forms.IntegerField(label="추가할 친구 ID")