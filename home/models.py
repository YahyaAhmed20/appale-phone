from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class CarouselItem(models.Model):
    title = models.CharField("Title", max_length=100)
    subtitle = models.CharField("Subtitle", max_length=200, blank=True, null=True)
    image = models.ImageField("Image", upload_to='carousel_images/')
    content = models.TextField("Content", blank=True, null=True)
    is_active = models.BooleanField("Active", default=True)
    order = models.PositiveIntegerField("Order", default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Slide"
        verbose_name_plural = "Slides Management"
        
        
class ShopSingle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    title = models.CharField("Product Name", max_length=200)
    # price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    # rating = models.FloatField("Rating", default=0.0, blank=True, null=True)
    # brand = models.CharField("Brand", max_length=100)
    # description = models.TextField("Description", blank=True, null=True)
    # available_colors = models.CharField(
    #     "Available Colors",
    #     max_length=200,
    #     help_text="Separate colors with commas, e.g.: Red, Blue, Green"
    # )
    image = models.ImageField("Product Image", upload_to='products/')
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Featured Product"