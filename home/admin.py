from django.contrib import admin
from .models import CarouselItem
from .models import ShopSingle

@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'subtitle')
    prepopulated_fields = {'subtitle': ('title',)}  # اختياري
    
    
    

@admin.register(ShopSingle)
class ShopSingleAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'brand', 'owner', 'rating')
    search_fields = ('title', 'brand', 'owner__username')
    list_filter = ('brand', 'owner')
    prepopulated_fields = {'description': ('title',)}  # اختياري