from django import forms
from .models import ShopSingle

class ShopSingleForm(forms.ModelForm):
    class Meta:
        model = ShopSingle
        fields = ['title', 'price', 'rating', 'brand', 'description', 'available_colors', 'owner', 'image']