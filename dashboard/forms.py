from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ['title', 'body', 'slug', 'img']
        widgets = {
            i: forms.TextInput(attrs={'class': 'form-control'}) for i in fields
        }
    
    
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError("Slug cannot be create")
        if Post.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError("Slug is alredy exists (Must be unicle)")
        else:
            return new_slug
