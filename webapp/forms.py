from django import forms

from .models import Post

class PostQueryForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'query', 'contact')