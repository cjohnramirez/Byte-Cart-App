from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
  path("", views.index, name="index"),
  path("<int:product_id>/", views.detail, name="detail"),
  path("<int:product_id>/review", views.review, name="review"),
]