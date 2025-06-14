from django.shortcuts import render
from .models import Shop
from django.core.paginator import Paginator
# Create your views here.
from .filters import ShopFilter

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