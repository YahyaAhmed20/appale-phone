from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
def upload_to(instance, filename):
    return f"job_images/{instance.slug}/{filename}"

def generate_unique_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = f"{slug}-{get_random_string(length=4)}"
        return generate_unique_slug(instance, new_slug=new_slug)
    return slug



class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    title = models.CharField("Product Name", max_length=200)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    brand = models.CharField("Brand", max_length=100)
    description = models.TextField("Description", blank=True, null=True)
    available_colors = models.CharField(
        "Available Colors",
        max_length=200,
        help_text="Separate colors with commas, e.g.: Red, Blue, Green"
    )
    image = models.ImageField("Product Image", upload_to='products/')
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)
    active=models.BooleanField(default=True,verbose_name=(("Active")))
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Discount Price",
        default=0.00
    )    
   
    isNew=models.BooleanField(default=True ,verbose_name=(("New Product")))
    isBestSeller=models.BooleanField(default=False ,verbose_name=(("Best Seller Product")))
    slug = models.SlugField(null=True,blank=True, help_text="Auto-generated slug for URLs")



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product Management"
        
        
class ProductImage(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return f"Image for {self.shop.title}"
    
    
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.transaction_id}"
