from.models import Shop

from django import forms




class Shopform(forms.ModelForm):
    class Meta:
        model=Shop
        fields='__all__'
        exclude=('owner','created_at','updated_at')
    