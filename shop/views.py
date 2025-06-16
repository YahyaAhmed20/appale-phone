from django.shortcuts import render
from .models import Shop
from django.core.paginator import Paginator
# Create your views here.
from .filters import ShopFilter
from django.shortcuts import render,get_object_or_404

def shop_list(request):
    products = Shop.objects.all()  # 1. هات كل المنتجات

    myfilter = ShopFilter(request.GET, queryset=products)  # 2. طبق الفلتر عليهم
    filtered_products = myfilter.qs  # 3. خزن النتيجة بعد الفلترة

    paginator = Paginator(filtered_products, 3)  # 4. اعمل pagination بعد الفلترة
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,  # المنتجات المتقسمة على صفحات
        'myfilter': myfilter,  # الفورم الخاص بالفلترة
    }

    return render(request, 'shop/shop_list.html', context)




def shop_detail(request, slug):
    # Fetch the job detail using the slug
    job_detail = get_object_or_404(Shop, slug=slug)

    images = job_detail.images.all()  # related_name='images' في الموديل الجانبي

    
    related_products = Shop.objects.filter(active=True).exclude(id=job_detail.id)[:3]

    # Pass the form and job detail to the template
    context = {'job_detail': job_detail,'images': images,'related_products': related_products}

    return render(request, 'shop/shop_detail.html', context)