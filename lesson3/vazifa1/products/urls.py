from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create),
    path('list/', list),
    path('detail/<int:pk>', detail),
    path('full_update/<int:pk>', full_update),
    path('pupdate/<int:pk>', partial_update),
    path('delete/<int:pk>', delete),
]