from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TimeField
from froala_editor.fields import FroalaField
from Blog.helper import *

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    create_at= models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    slug= models.SlugField(max_length=100,null=True, blank=True)
    content = FroalaField()
    image = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.title
    def save(self,*args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)