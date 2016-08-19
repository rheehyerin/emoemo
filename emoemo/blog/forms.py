from django import forms
from .models import Post
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    tag_names = forms.CharField()

    class Meta:
        model = Post
        fields = ['content']

    def clean_tag_names(self):
        tag_names = self.cleaned_data.get('tag_names', '')
        return tag_names.split()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]