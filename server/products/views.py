from django.http import HttpResponse

def product(product_id):
    return HttpResponse(f'Products Loaded!')

def detail(request, product_id):
    response = f"You're looking at the details of product {product_id}"
    return HttpResponse(response)

def review(request, product_id):
    return HttpResponse(f"You're reviewing product {product_id}") 

# Create your views here.
