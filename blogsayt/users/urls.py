from django.urls import path
from .views import *

urlpatterns = [
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='signin'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='update'),
    path('pass-change/', PasswordUpdateView.as_view(), name='pass-change'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


