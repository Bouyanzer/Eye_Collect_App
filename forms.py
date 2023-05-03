from dataclasses import fields
from pyexpat import model
from django import forms 
from .models import *


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Oeil
        fields = ('image_L','stade_L', 'image_R','stade_R')
