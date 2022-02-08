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