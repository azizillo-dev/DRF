from django.urls import path
from .views import *

urlpatterns = [
    path('lcreate/', UsersListCreateView.as_view()),
]