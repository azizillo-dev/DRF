from django.urls import path
from .views import *


urlpatterns = [
    path('products/create/', ProductCreateApiView.as_view()),
    path('products/', ProductListApiView.as_view()),
    path('products/<int:pk>/', ProductDetailApiView.as_view()),
    path('products/<int:pk>/update/', ProductUpdateApiView.as_view()),
    path('products/<int:pk>/delete/', ProductDeleteApiView.as_view()),
]