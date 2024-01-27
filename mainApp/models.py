from django.db import models
from tinymce.models import HTMLField


class Gallery(models.Model):
   id=models.AutoField(primary_key=True)
   photo=models.ImageField(upload_to="uploads")

class Contact(models.Model):
   id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=100)
   email=models.EmailField()
   phone=models.CharField(max_length=10)
   subject=models.CharField(max_length=100)
   message=models.TextField()
   def __str__(self):
     return str(self.name)


class Blog(models.Model):
     id=models.AutoField(primary_key=True)
     title=models.CharField(max_length=200)
     image=models.ImageField(upload_to="uploads")
     description=HTMLField()
     date=models.DateField(auto_now=True)
     meta_description=models.TextField(default='',null=True,blank=True)
     meta_keyword=models.TextField(default='',null=True,blank=True)
     def __str__(self):
         return str(self.title)
