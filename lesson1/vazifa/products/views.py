from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from rest_framework import status
import json

@api_view(["GET"])
def hello_api(request):
    return Response({
        'msg' : 'Hello DRF'
    })




@api_view(["GET"])
def test_api(request):
    return Response(
        {
            "msg" : "Bu test API",
            "name" : "Azizillo",
            "age" : 19,
            "skill" : "Backend Engineer"
        }
    )



@api_view(["POST"])
def create_product(request):

    title = request.data.get('title')
    price = request.data.get('price')   
    desc = request.data.get('desc')


    Product.objects.create(title=title, price=price, desc=desc)

    return Response({
        'msg' : "Yaratildi",
    },
    status=status.HTTP_201_CREATED
    )



@api_view(["GET"])
def products_detail(request, pk):
    product = Product.objects.get(pk=pk)


    return Response(
        {
            'msg' : "Yuborildi",
            'product' : {
                'id' : product.id,
                'title' : product.title,
                'price' : product.price,
                'desc' : product.desc,
            }
        },
        status=status.HTTP_200_OK
    )





@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()

    data = []
    for product in products:
        data.append({
            'id' : product.id,
            'title' : product.title,
            'price' : product.price,
            'decs' : product.desc,
        })

    return Response({
        "msg" : "Jami productlar",
        'products' : data
    }, status=status.HTTP_200_OK
    )















