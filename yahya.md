

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








   shop _detail 




   طيب هنا لما بعمل add to cart ف رساله بتظهرلي بس بعديها مش بعرف اتحكم ف navbar لاازم اعمل refresh الموقع بيقف {% extends 'base.html' %}
{% load static %}
{% block body %}
{% load custom_filters %}

{% if messages %}
  <div id="message-container" class="d-flex justify-content-center w-100 position-fixed top-0 start-0 p-3" style="z-index: 9999;">
    <div style="min-width: 300px; max-width: 600px;">
      {% for message in messages %}
        <div class="alert alert-success alert-dismissible fade show text-center shadow" role="alert">
          {{ message }}
        </div>
      {% endfor %}
    </div>
  </div>

  <script>
    setTimeout(() => {
      const messages = document.querySelectorAll('#message-container .alert');
      messages.forEach(msg => {
        msg.classList.remove('show');
        msg.classList.add('fade');
      });
    }, 5000);
  </script>
{% endif %}


<!-- Open Content -->
<section class="bg-light">
    <div class="container pb-5">
        <div class="row">
            <!-- Product Image -->
            <div class="col-lg-5 mt-5" data-aos="fade-right">
                <div class="card mb-3">
                    <img class="card-img img-fluid mb-3" src="{{ job_detail.image.url }}" alt="{{ job_detail.title }}" id="product-detail">
                </div>

                <!-- Carousel -->
                <div class="row align-items-center">
                    <div class="col-1 text-center">
                        <a href="#multi-item-example" role="button" data-bs-slide="prev">
                            <i class="text-dark fas fa-chevron-left fa-lg"></i>
                        </a>
                    </div>

                    <div id="multi-item-example" class="col-10 carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
                        <div class="carousel-inner product-links-wap" role="listbox">
                            {% if images %}
                                {% for img in images %}
                                    {% if forloop.counter0|divisibleby:3 %}
                                        <div class="carousel-item {% if forloop.first %}active{% endif %}">
                                            <div class="row">
                                    {% endif %}
                                    <div class="col-4 mb-2" data-aos="zoom-in">
                                        <a href="{{ img.image.url }}" target="_blank">
                                            <img class="card-img img-fluid border" src="{{ img.image.url }}" alt="Extra Image {{ forloop.counter }}">
                                        </a>
                                    </div>
                                    {% if forloop.counter|divisibleby:3 or forloop.last %}
                                            </div>
                                        </div>
                                    {% endif %}
                                {% endfor %}
                            {% else %}
                                <div class="carousel-item active">
                                    <div class="col-12">
                                        <p>No additional images available.</p>
                                    </div>
                                </div>
                            {% endif %}
                        </div>
                    </div>

                    <div class="col-1 align-self-center">
                        <a href="#multi-item-example" role="button" data-bs-slide="next">
                            <i class="text-dark fas fa-chevron-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Product Info -->
            <div class="col-lg-7 mt-5" data-aos="fade-left">
                <div class="card">
                    <div class="card-body">
                        <h1 class="h2">{{ job_detail.title }}</h1>
{% if job_detail.discount > 0 %}
    <p class="h3 py-2">
        <del class="text-muted">${{ job_detail.price }}</del><br>
        <span class="text-success fw-bold">
            ${{ job_detail.price|subtract:job_detail.discount|floatformat:2 }}
        </span>
    </p>
{% else %}
    <p class="h3 py-2">${{ job_detail.price }}</p>
{% endif %}
                        <ul class="list-inline">
                            <li class="list-inline-item">
                                <h6>Brand:</h6>
                            </li>
                            <li class="list-inline-item">
                                <p class="text-muted"><strong>{{ job_detail.brand }}</strong></p>
                            </li>
                        </ul>
{% if job_detail.available_colors %}
    <ul class="list-inline">
        <li class="list-inline-item">
            <h6>Available Colors:</h6>
        </li>
        {% for color in job_detail.available_colors|split:"," %}
            <li class="list-inline-item">
                <span class="badge bg-primary text-white">{{ color|trim }}</span>
            </li>
        {% endfor %}
    </ul>
{% endif %}
                        <h6>Description:</h6>
                        <p>{{ job_detail.description }}</p>

                        <form method="post" action="{% url 'shop:add_to_cart' job_detail.id %}">
    {% csrf_token %}

    <div class="row">
        <div class="col-auto">
            <ul class="list-inline pb-3">
                <li class="list-inline-item text-right">
                    Quantity
                    <input type="hidden" name="product-quanity" id="product-quanity" value="1">
                </li>
                <li class="list-inline-item"><span class="btn btn-success" id="btn-minus">-</span></li>
                <li class="list-inline-item"><span class="badge bg-secondary" id="var-value">1</span></li>
                <li class="list-inline-item"><span class="btn btn-success" id="btn-plus">+</span></li>
            </ul>
        </div>
    </div>

    <div class="row pb-3">
        <div class="col d-grid">
            <button type="submit" class="btn btn-success btn-lg" name="submit" value="cart">Add to Cart</button>
        </div>
    </div>
</form>

                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Related Products -->
<section class="py-5">
    <div class="container">
        <div class="row text-left p-2 pb-3">
            <h4 data-aos="fade-up">Related Products</h4>
        </div>

        <div id="carousel-related-product" class="row g-4"> <!-- أضفنا g-4 هنا -->
            {% if related_products %}
                {% for product in related_products %}
                    <div class="col-md-4" data-aos="fade-up" data-aos-delay="{{ forloop.counter0|add:1 }}00">
                        <div class="product-wap card rounded-0 h-100">
                            <div class="card rounded-0">
                                <img class="card-img-top img-fluid" src="{{ product.image.url }}" alt="{{ product.title }}" style="height: 250px; object-fit: contain; object-position: center;">
                                <div class="card-img-overlay rounded-0 product-overlay d-flex align-items-center justify-content-center">
                                    <ul class="list-unstyled">
                                        <li>
                                            <a class="btn btn-success text-white mt-2" href="{% url 'shop:shop_detail' product.slug %}">
                                                <i class="far fa-eye"></i>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="card-body">
                                <a href="{% url 'shop:shop_detail' product.slug %}" class="h3 text-decoration-none">{{ product.title }}</a>
                                <p class="text-center mb-0">${{ product.price }}</p>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            {% else %}
                <p>No related products available.</p>
            {% endif %}
        </div>
    </div>
</section>


<!-- AOS Script -->
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
<script>
  AOS.init({
    duration: 600,
    once: true
  });
</script>

{% endblock body %}
