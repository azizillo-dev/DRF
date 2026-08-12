from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import get_object_or_404

@api_view(['POST'])
def create_product(request):
    model = request.data.get('model')
    name = request.data.get('name')
    description = request.data.get('description')
    price = request.data.get('price')
    display = request.data.get('display')

    Product.objects.create(
        model=model,
        name=name,
        description=description,
        price=price,
        display=display
    )

    return Response({
        'msg' : 'Product created',
    }, status=status.HTTP_201_CREATED)
    


@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'model': product.model,
            'name': product.name,
            'description': product.description,
            'price': str(product.price), 
            'display': product.display,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        })
    
    return Response({
        'count': len(data),
        'products': data
    }, status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({
            'error' : 'Mahsulot topilmadi'
        }, status=status.HTTP_404_NOT_FOUND)

    if 'model' in request.data:
        product.model = request.data['model']
    if 'name' in request.data:
        product.name = request.data['name']
    if 'description' in request.data:
        product.name = request.data['description']
    if 'price' in request.data:
        product.name = request.data['price']
    if 'display' in request.data:
        product.name = request.data['display']

    product.save()

    return Response({
        'message': 'Product updated',
        'id': product.id,
        'model': product.model,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'display': product.display,
    }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response({
        'msg' : 'Product deleted',
        'id' : product.id
    }, status=200)





@api_view(['GET'])
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data ={
        'id': product.id,
        'model': product.model,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'display': product.display,
        'created_at' : product.created_at
    }
    return Response(data, status=200)







