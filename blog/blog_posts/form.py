from django import forms
from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('user_name', 'user_email', 'text_comments')