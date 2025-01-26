from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Product(models.Model):
  product_name = models.CharField(max_length=200)
  product_date = models.DateTimeField("date published")

  def __str__(self):
    return self.product_name
  
  def was_published_recently(self):
    return self.product_date >= timezone.now() - datetime.timedelta(days = 1)

class ProductReviews(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  product_review_text = models.CharField(max_length=200)
  product_rating = models.IntegerField(default=0)

  def __str__(self):
    return str(self.product)