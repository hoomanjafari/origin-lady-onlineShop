from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('products/', views.ShopTshirtView.as_view(), name='tshirt'),
    path('product/details/<int:pk>/', views.ProductDetails.as_view(), name='product_details'),
]
