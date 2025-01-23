from django.http import HttpResponse
from .models import Product

def product(product_id):
    return HttpResponse(f'Products Loaded!')

def detail(request, product_id):
    response = f"You're looking at the details of product {product_id}"
    return HttpResponse(response)

def review(request, product_id):
    return HttpResponse(f"You're reviewing product {product_id}") 

def index(request):
    latest_product_list = Product.objects.order_by("product_id")[:5]
    output = ", ".join([q.product_name for q in latest_product_list])
# Create your views here.
