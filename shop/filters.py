import django_filters
from .models import Shop


class ShopFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
   
    
    class Meta:
        model = Shop
        fields = '__all__'
        
        exclude=['owner','image','updated_at','created_at','available_colors','description','cost','discount','isNew','isBestSeller']