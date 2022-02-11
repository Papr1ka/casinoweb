from dataclasses import fields
from django import forms
from .models import Command, Post, TextCallback
from django.core.exceptions import ValidationError
from markdown import markdown


class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ['title', 'body', 'slug', 'img']
        widgets = {
            i: forms.TextInput(attrs={'class': 'linear'}) for i in fields
        }
        
        widgets['body'] = forms.Textarea(attrs={'class': 'body_editor', 'wrap': 'off', 'placeholder': '#markdown here'})
    
    
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError("Slug cannot be create")
        if Post.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError("Slug is alredy exists (Must be unicle)")
        else:
            return new_slug

class CommandForm(forms.ModelForm):
    
    class Meta():
        model = Command
        fields = ['name', 'usage', 'example', 'dop', 'category']
        widgets = {
            i: forms.TextInput(attrs={'class': 'linear'}) for i in fields
        }

class TextCallbackForm(forms.ModelForm):
    
    class Meta():
        model = TextCallback
        fields = ['author', 'text', 'contact']
        widgets = {
            i: forms.TextInput(attrs={'class': 'linear'}) for i in fields
        }
        widgets['text'] = forms.Textarea(attrs={'class': 'body_editor', 'wrap': 'off', 'placeholder': '#Ваша обратная связь здесь'})