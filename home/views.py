from django.shortcuts import render
from .models import CarouselItem
from .models import ShopSingle

# Create your views here.

def home(request):
    
    
    carousel_items = CarouselItem.objects.filter(is_active=True)

    products = ShopSingle.objects.all()

    
    return render(request, 'home/home.html', {
        'carousel_items': carousel_items,
        'products': products
    })