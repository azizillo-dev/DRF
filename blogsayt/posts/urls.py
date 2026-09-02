from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('list/', PostListView.as_view(), name='list-posts'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update-post'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete-post'),
]