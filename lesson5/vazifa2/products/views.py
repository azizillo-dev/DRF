from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Product
from rest_framework.generics import get_object_or_404



class ProductCRUDView(ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serrializer = ProductSerializer(instance=product, data=request.data)
        serrializer.is_valid(raise_exception=True)
        serrializer.save()
        return Response(serrializer.data)

    def partial_update(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({"message": "Product deleted successfully"})

    




