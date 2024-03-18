from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('products/tshirt/', views.ShopTshirtView.as_view(), name='shop_tshirt'),
    path('products/beach_shirt/', views.ShopBeachShirtView.as_view(), name='shop_beach_shirt'),
    path('products/hats/', views.ShopHatsView.as_view(), name='shop_hats'),
    path('products/legs/', views.ShopLegsView.as_view(), name='shop_legs'),
    path('products/shomiz/', views.ShopShomizView.as_view(), name='shop_shomiz'),
    path('products/tops/', views.ShopTopsView.as_view(), name='shop_tops'),
    path('products/under_wear/', views.ShopUnderWearView.as_view(), name='under_wear'),
    path('product/details/<int:pk>/', views.ProductDetails.as_view(), name='product_details'),
    path('checkout/', views.CheckOutView.as_view(), name='checkout'),
    path('cart_item_remove/<int:pk>/', views.RemoveCartItem.as_view(), name='remove_cart_items'),
    path('get_edited_id/', views.get_edited_item_id, name='get_edited_item_id'),
    path('edit_cart_item/', views.EditItemCartView.as_view(), name='edit_cart_item'),
    path('search_result/', views.SearchView.as_view(), name='search_result'),
]
