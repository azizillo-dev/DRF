from .serializers import ProductSerializer
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404




class ProductCreateAPIView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg' : 'Product created successfully!',
            "product" : serializer.data
        }, status=201)



class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response({
            "msg" : "Products list",
            "products" : serializer.data
        }, status=200)


class ProductUpdateAPIView(APIView):
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "msg" : "Product updated successfully!",
            "product" : serializer.data
        }, status=200)



class ProductPartialUpdateAPIView(APIView):
    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(data=request.data, instance=product, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "msg" : "Product partially updated successfully!",
            "product" : serializer.data
        }, status=200)



class ProductDeleteAPIView(APIView):
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({
            "msg" : "Product deleted successfully!"
        }, status=204)



    
    
    
        