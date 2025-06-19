# admin.py
from django.contrib import admin
from .models import Shop, ProductImage,Order  

class ProductImageInline(admin.TabularInline):  # أو admin.StackedInline لو حابب شكل تاني
    model = ProductImage
    extra = 1  # عدد الصور الفاضية الجاهزة للإضافة

class ShopAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Shop, ShopAdmin)
admin.site.register(ProductImage)  # لو حابب تتحكم فيها بشكل مستقل كمان



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'transaction_id', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'transaction_id')