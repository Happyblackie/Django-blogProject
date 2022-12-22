from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Article1(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add thumbnail later
    thumb = models.ImageField(default='default.png',blank=True)
    #add author later
    #author = models.ForeignKey(User,default=None) -> this one works for only django 1
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        #return str (self.title)
        return self.title
        
    def snippet(self):
        return self.body[:10] + "...." 