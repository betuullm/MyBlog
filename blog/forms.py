from django import forms
from .models import Post, PostImage
from django.forms import modelformset_factory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'quill-editor'}),
        }

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

PostImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=3, max_num=10)
