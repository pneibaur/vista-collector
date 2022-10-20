from dataclasses import field
from django.forms import ModelForm
from .models import Comment, Flair

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment",]

class FlairForm(ModelForm):
    class Meta:
        model = Flair
        fields = ['tag',]