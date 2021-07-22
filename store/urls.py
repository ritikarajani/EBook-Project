from django.urls import path
from . import views 

urlpatterns = [
path('', views.store_homepage),
# path('1', views.product_1_view),
path('add_cart_item/', views.add_cart_item),
path('cart/', views.cart_view),
path('cart/del_cart_item/',views.del_cart_item),
]