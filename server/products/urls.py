from django.urls import path
from . import views

urlpatterns = [
  path("", views.product, name="product"),
  path("<int:product_id>/", views.detail, name="detail"),
  path("<int:product_id>/review", views.review, name="review"),
]