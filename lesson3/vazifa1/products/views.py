from django.core.management.base import AppCommand
from operator import truediv
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['POST'])
def create(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({
        'msg' : 'Product created',
        'product' : serializer.data
    }, status=201)



@api_view(['GET'])
def list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response({
        "msg" : "Products list",
        "count" : len(products),
        "products" : serializer.data
    }, status=200)
    




@api_view(['GET'])
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    serializer = ProductSerializer(product)

    return Response({
        'msg' : "Product",
        "product" : serializer.data
    }, status=200)


@api_view(['PUT'])
def full_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(

    )
    return Response({
        "msg" : "Product updated",
        "product" : serializer.data
    }, status=200)
   



@api_view(['PATCH'])
def partial_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(instance=product, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({
        "msg" : "Product p updated",
        "product" : serializer.data
    }, status=200)




@api_view(['DELETE'])
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response({
        "msg" : "Product deleted"
    }, status=200)










