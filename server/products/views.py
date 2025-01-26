from django.http import HttpResponse, Http404
from .models import Product, ProductReviews
from django.shortcuts import render, get_object_or_404

def product(product_id):
    return HttpResponse(f'Products Loaded!')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {
        "product_name": Product.objects.get(id=product_id),
        "product_review": ProductReviews.objects.get(product=product_id)
    }) 
    #dictionary can be directly put as argument to 3rd param

def review(request, product_id):
    return HttpResponse(f"You're reviewing product {product_id}") 

def index(request):
    latest_product_list = Product.objects.order_by("id")
    context = {"latest_product_list": latest_product_list} 
    return render(request, "products/index.html", context)
    # 1st arg: request object, 2nd arg: template name, 3rd arg: dictionary (optional)

