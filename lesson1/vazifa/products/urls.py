from django.urls import path
from .views import *


urlpatterns = [
    path('hello/', hello_api),
    path('test/', test_api),
    path('create/', create_product),
    path('detail/<int:pk>', products_detail),
    path('list/', product_list),
]














