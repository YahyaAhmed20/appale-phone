بكره هنشتغل علي shop _detail 

ونربط كل حاجه  ب models 


2 
عايزين نضيف profile (signin and signup )

3 - 
نضيف ف shop_detial button add to card 

4- 
لما user يضغط علي add to card يظهرله الحاجه الي ضافها ويلاقي ظرار اسمه process continue  ده هيلاقي فيه shop summry فيه الحاجات الي حجزها من الموقع وفيه زراراين checkout ,return to shop 












shop_list





{% extends 'base.html' %}
{% load static %}
{% load custom_filters %}
{% block body %}
{% load widget_tweaks %}

{% load bootstrap4 %}


    <!-- Start Content -->
   <div class="container py-5">    
  <div class="row">
    <!-- الفلتر -->
    <div class="col-lg-3">
      <div class="card shadow-sm">
        <div class="card-body">
          <h4 class="mb-3">Filter</h4>
          <form method="GET">
            {% for field in myfilter.form %}
              <div class="mb-3">
                <label class="form-label">{{ field.label }}</label>
                {{ field|add_class:"form-control" }}
              </div>
            {% endfor %}
            <button type="submit" class="btn btn-primary w-100 mt-2">بحث</button>
            <a href="{% url 'shop:shop_list' %}" class="btn btn-secondary w-100 mt-2">إعادة المحاولة</a>

          </form>
        </div>
      </div>
    </div>


            <div class="col-lg-9">
                <div class="row">
                  
                    <div class="col-md-6 pb-4">
                       
                    </div>
                </div>
     <div class="row">
    {% if products %}
        {% for product in products %}
            <div class="col-md-4">
                <div class="card mb-4 product-wap rounded-0 h-100 shadow-sm">

                    <!-- جزء الصورة + بادجات -->
                    <div class="position-relative product-img-container">
                        <a href="{% url 'shop:shop_detail' product.slug %}">
                            {% if product.image %}
                                <img class="card-img-top product-img" src="{{ product.image.url }}" alt="{{ product.title }}">
                            {% else %}
                                <img class="card-img-top product-img" src="https://via.placeholder.com/300x300" alt="No Image">
                            {% endif %}
                        </a>

                        <!-- البادجات -->
                        <div class="position-absolute top-0 start-0 m-2 d-flex flex-column gap-1">
                            {% if product.isNew %}
                                <span class="badge bg-success">New</span>
                            {% endif %}
                            {% if product.isBestSeller %}
                                <span class="badge bg-warning text-dark">Best Seller</span>
                            {% endif %}
                           
                        </div>
                    </div>

                    <!-- تفاصيل المنتج -->
                    <div class="card-body text-center">
                        <!-- اسم المنتج -->
                        <a href="{% url 'shop:shop_detail' product.slug %}" class="h5 text-decoration-none fw-bold text-dark">{{ product.title }}</a>

                        <!-- السعر -->
                        <p class="mb-2 mt-2">
                           {% if product.discount > 0 %}
        <del class="text-muted">${{ product.price }}</del><br>
        <span class="text-success fw-bold fs-5">
            ${{ product.price|subtract:product.discount|floatformat:2 }}
        </span>
    {% else %}
        <span class="fw-bold fs-5">${{ product.price }}</span>
    {% endif %}
                        </p>

                        <!-- الألوان المتاحة -->
                       

                        <!-- زر التفاصيل -->
                        <div>
                            <a href="{% url 'shop:shop_detail' product.slug %}" class="btn btn-sm btn-outline-primary">المزيد من التفاصيل</a>
                        </div>
                    </div>
                </div>
            </div>
        {% endfor %}
    {% else %}
        <div class="col-12">
            <p class="text-center">لا توجد منتجات حالياً</p>
        </div>
    {% endif %}
</div>



<!-- Pagination -->
            {% if products.has_other_pages %}
            <div class="row mt-4">
                <div class="col-lg-12">
                    <div class="pagination_wrap d-flex justify-content-center">
                        <ul class="pagination">
                            {% if products.has_previous %}
                            <li class="page-item">
                                <a href="?page={{ products.previous_page_number }}" class="page-link" aria-label="Previous">
                                    <i class="ti-angle-left"></i> Previous
                                </a>
                            </li>
                            {% else %}
                            <li class="page-item disabled">
                                <span class="page-link"><i class="ti-angle-left"></i> Previous</span>
                            </li>
                            {% endif %}

                            {% for i in products.paginator.page_range %}
                            <li class="page-item {% if products.number == i %}active{% endif %}">
                                <a href="?page={{ i }}" class="page-link">{{ i }}</a>
                            </li>
                            {% endfor %}

                            {% if products.has_next %}
                            <li class="page-item">
                                <a href="?page={{ products.next_page_number }}" class="page-link" aria-label="Next">
                                    Next <i class="ti-angle-right"></i>
                                </a>
                            </li>
                            {% else %}
                            <li class="page-item disabled">
                                <span class="page-link">Next <i class="ti-angle-right"></i></span>
                            </li>
                            {% endif %}
                        </ul>
                    </div>
                </div>
            </div>
            {% endif %}
        </div>
    </div>
</div>
<!-- End Content -->


    <!-- End Content -->

    <!-- Start Brands -->
    <section class="bg-light py-5">
        <div class="container my-4">
            <div class="row text-center py-3">
                <div class="col-lg-6 m-auto">
                    <h1 class="h1">Our Brands</h1>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                        Lorem ipsum dolor sit amet.
                    </p>
                </div>
                <div class="col-lg-9 m-auto tempaltemo-carousel">
                    <div class="row d-flex flex-row">
                        <!--Controls-->
                        <div class="col-1 align-self-center">
                            <a class="h1" href="#multi-item-example" role="button" data-bs-slide="prev">
                                <i class="text-light fas fa-chevron-left"></i>
                            </a>
                        </div>
                        <!--End Controls-->

                        <!--Carousel Wrapper-->
                        <div class="col">
                            <div class="carousel slide carousel-multi-item pt-2 pt-md-0" id="multi-item-example" data-bs-ride="carousel">
                                <!--Slides-->
                                <div class="carousel-inner product-links-wap" role="listbox">

                               <div class="carousel-item active">
                                        <div class="row">
                                            <div class="col-3 p-md-5">
                                                <a href="#">
                                                    <img class="img-fluid brand-img" src="{% static 'assets/img/brand_01.png' %}" alt="Brand Logo">
                                                </a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#">
                                                    <img class="img-fluid brand-img" src="{% static 'assets/img/brand_02.png' %}" alt="Brand Logo">
                                                </a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#">
                                                    <img class="img-fluid brand-img" src="{% static 'assets/img/brand_03.png' %}" alt="Brand Logo">
                                                </a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#">
                                                    <img class="img-fluid brand-img" src="{% static 'assets/img/brand_04.png' %}" alt="Brand Logo">
                                                </a>
                                            </div>
                                        </div>
                                    </div>

                                    <!--End First slide-->

                                    <!--Second slide-->
                                    <div class="carousel-item">
                                        <div class="row">
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_01.png' %}" alt="Brand Logo"></a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_02.png' %}" alt="Brand Logo"></a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_03.png' %}" alt="Brand Logo"></a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_04.png' %}" alt="Brand Logo"></a>
                                            </div>
                                        </div>
                                    </div>
                                    <!--End Second slide-->

                                    <!--Third slide-->
                                    <div class="carousel-item">
                                        <div class="row">
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_01.png' %}" alt="Brand Logo"></a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_02.png' %}" alt="Brand Logo"></a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_03.png' %}" alt="Brand Logo"></a>
                                            </div>
                                            <div class="col-3 p-md-5">
                                                <a href="#"><img class="img-fluid brand-img" src="{% static 'assets/img/brand_04.png' %}" alt="Brand Logo"></a>
                                            </div>
                                        </div>
                                    </div>
                                    <!--End Third slide-->

                                </div>
                                <!--End Slides-->
                            </div>
                        </div>
                        <!--End Carousel Wrapper-->

                        <!--Controls-->
                        <div class="col-1 align-self-center">
                            <a class="h1" href="#multi-item-example" role="button" data-bs-slide="next">
                                <i class="text-light fas fa-chevron-right"></i>
                            </a>
                        </div>
                        <!--End Controls-->
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!--End Brands-->



<style>
.product-img-container {
    height: 500px; /* قللنا الارتفاع بدل 250 */
    width: 100%;
    aspect-ratio: 1 / 1; /* تحافظ على شكل مربع تلقائياً */
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f8f8f8;
    overflow: hidden;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
}

.product-img {
    width: 100%;
    height: 140%;
    object-fit: contain;
    transition: transform 0.3s ease;
}

.product-img:hover {
    transform: scale(1.05); /* تأثير بسيط لو تحب */


}

.card-body {
    min-height: 150px; /* أو حسب ما يناسبك */
}

</style>

   {% endblock body %}