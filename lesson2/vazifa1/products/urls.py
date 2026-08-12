from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create_product),
    path('products-list/', products_list),
    path('update/<int:pk>', product_update),
    path('delete/<int:pk>', delete),
    path('detail/<int:pk>', detail),
]