from django.http import HttpResponse
from products.models import Product
from django.template import loader

def product(product_id):
    return HttpResponse(f'Products Loaded!')

def detail(request, product_id):
    response = f"You're looking at the details of product {product_id}"
    return HttpResponse(response)

def review(request, product_id):
    return HttpResponse(f"You're reviewing product {product_id}") 

def index(request):
    latest_product_list = Product.objects.order_by("id")
    template = loader.get_template("products/index.html")
    context = {
        "latest_product_list": latest_product_list,
    } 
    return HttpResponse(template.render(context, request))
# Create your views here.
