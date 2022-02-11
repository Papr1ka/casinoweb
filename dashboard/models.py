from time import time
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from markdown import markdown


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    img = models.URLField(max_length=300)
    date_pub = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})
    
    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})
    
    def gen_slug(self, s):
        new_slug = slugify(s, allow_unicode=True)
        return new_slug + '-' + str(time())
    
    def save(self, *args, **kwargs):
        if not self.id or self.slug == '':
            self.slug = self.gen_slug(self.title)
        super().save(*args, **kwargs)
    
    def raw(self):
        return markdown(self.body)

    class Meta:
        ordering = ['-date_pub']

class Command(models.Model):
    name = models.SlugField(unique=True)
    usage = models.TextField()
    example = models.TextField()
    dop = models.TextField(blank=True)
    category = models.TextField()
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse('command_update_url', kwargs={'name': self.name})
    
    def get_delete_url(self):
        return reverse('command_delete_url', kwargs={'name': self.name})

    def get_absolute_url(self):
        return reverse("commands_url")

class TextCallback(models.Model):
    text = models.TextField()
    author = models.TextField()
    contact = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("textcallback_url", kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('textcallback_delete_url', kwargs={'slug': self.slug})
    
    def gen_slug(self, s):
        new_slug = slugify(s, allow_unicode=True)
        return new_slug + '-' + str(time())
    
    def save(self, *args, **kwargs):
        self.slug = self.gen_slug(self.text)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_pub']
