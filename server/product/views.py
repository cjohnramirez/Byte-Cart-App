from product.models import Product
from product.serializers import ProductSerializer
from rest_framework import generics

#List: GET, Create: POST
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#Retrive: GET, Update: PUT, Destroy: DELETE
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer