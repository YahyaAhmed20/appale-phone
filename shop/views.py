from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop,Order
from django.core.paginator import Paginator
from .filters import ShopFilter
from django.contrib import messages  # أعلى الملف
from django.contrib.auth.decorators import login_required


def shop_list(request):
    products = Shop.objects.all()
    myfilter = ShopFilter(request.GET, queryset=products)
    filtered_products = myfilter.qs

    paginator = Paginator(filtered_products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'myfilter': myfilter,
    }
    return render(request, 'shop/shop_list.html', context)


def shop_detail(request, slug):
    job_detail = get_object_or_404(Shop, slug=slug)
    images = job_detail.images.all()
    related_products = Shop.objects.filter(active=True).exclude(id=job_detail.id)[:3]

    context = {
        'job_detail': job_detail,
        'images': images,
        'related_products': related_products,
    }
    return render(request, 'shop/shop_detail.html', context)


@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    request.session.modified = True

    product = Shop.objects.get(id=product_id)
    messages.success(request, f"✅ {product.title} was added to your cart.")

    return redirect('shop:shop_detail', slug=product.slug)

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id_str, quantity in cart.items():
        try:
            product = Shop.objects.get(id=int(product_id_str))
            total_price = product.price * quantity
            total += total_price
            products.append({
                'product': product,
                'quantity': quantity,
                'total_price': total_price,
            })
        except Shop.DoesNotExist:
            continue

    context = {
        'products': products,
        'total': total,
    }
    return render(request, 'shop/cart.html', context)



def update_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        for key in cart.keys():
            qty_key = f'qty_{key}'
            if qty_key in request.POST:
                try:
                    qty = int(request.POST[qty_key])
                    if qty > 0:
                        cart[key] = qty
                    else:
                        cart.pop(key)  # لو الكمية 0 إحذف المنتج
                except ValueError:
                    continue
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('shop:view_cart')



def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('shop:view_cart')


def checkout(request):
    cart = request.session.get('cart', {})
    total = 0
    for product_id_str, quantity in cart.items():
        try:
            product = Shop.objects.get(id=int(product_id_str))
            total += product.price * quantity
        except Shop.DoesNotExist:
            continue

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        transaction_id = request.POST['transaction_id']

        user = request.user if request.user.is_authenticated else None

        Order.objects.create(
            name=name,
            phone=phone,
            transaction_id=transaction_id,
            total=total,
            status='pending',
            user=user,

        )

        request.session['cart'] = {}
        request.session.modified = True

        messages.success(request, "✅ Order received! Please wait while we confirm your payment.")
        return redirect('shop:shop_list')

    return render(request, 'shop/checkout.html', {'total': total})




@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/my_orders.html', {'orders': orders})