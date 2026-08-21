from rest_framework.routers import DefaultRouter
from .views import ProductCRUDView

router = DefaultRouter()

router.register('products', ProductCRUDView, basename='product')

urlpatterns = router.urls