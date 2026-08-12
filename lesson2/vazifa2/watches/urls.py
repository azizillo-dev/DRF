from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create_watch, name='create_watch'),
    path('detail/<int:pk>', watch_detail, name='detail_watch'),
    path('list/', watches_list, name='list_watch'),
    path('delete/<int:pk>', delete_watch, name='delete_watch'),
    path('update/<int:pk>', update_watch, name='update_watch')
]

