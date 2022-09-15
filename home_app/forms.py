from dataclasses import field
from operator import mod
from secrets import choice
from socket import fromshare
from tkinter import Widget
from tkinter.tix import Select
from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','body','category')
        
        widgets = {
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'})
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('body','category')
        
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
        }
