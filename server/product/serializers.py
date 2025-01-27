from rest_framework import serializers
from product.models import Product, ProductCategory, Discount

class ProductSerializer(serializers.ModelSerializer):
 class Meta:
  model = Product
  fields = '__all__'