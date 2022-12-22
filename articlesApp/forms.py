from django import forms
from .import models

#creating a model form
class CreateArticle(forms.ModelForm):
    #inside class Meta we define fields
    class Meta:
        model = models.Article1 # model from models.py
        fields = ['title','slug','body','thumb'] #fields from our model