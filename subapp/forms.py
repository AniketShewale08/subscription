from django import forms
from .models import Product

class RatingForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['ratings']
