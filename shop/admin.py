# admin.py
from django.contrib import admin
from .models import Shop, ProductImage

class ProductImageInline(admin.TabularInline):  # أو admin.StackedInline لو حابب شكل تاني
    model = ProductImage
    extra = 1  # عدد الصور الفاضية الجاهزة للإضافة

class ShopAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Shop, ShopAdmin)
admin.site.register(ProductImage)  # لو حابب تتحكم فيها بشكل مستقل كمان
