from django.shortcuts import render
from .models import Watch
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response



@api_view(['POST'])
def create_watch(request):

    brand = request.data.get('brand')
    model = request.data.get('model')
    description = request.data.get('description')
    price = request.data.get('price')
    screensize = request.data.get('screensize')
    mechanism = request.data.get('mechanism')
    water_resistant = request.data.get('water_resistant', False)

    try:
        Watch.objects.create(
            brand=brand,
            model=model,
            description=description,
            price=price,
            screensize=screensize,
            mechanism=mechanism,
            water_resistant=water_resistant
        )
        return Response({
            'msg' : 'Yaratildi'
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({
            'msg' : 'Xatolik'
        }, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def watch_detail(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    data = {
        'id' : watch.id,
        'brand' : watch.brand,
        'model' : watch.model,
        'description' : watch.description,
        'price' : watch.price,
        'screensize' : watch.screensize,
        'mechanism' : watch.mechanism,
        'water_resistant' : watch.water_resistant
    }
    return Response(data, status=200)






@api_view(['GET'])
def watches_list(request):
    watches = Watch.objects.all()
    data = []
    for watch in watches:
        data.append({
            'id' : watch.id,
            'brand' : watch.brand,
            'model' : watch.model,
            'description' : watch.description,
            'price' : watch.price,
            'screensize' : watch.screensize,
            'mechanism' : watch.mechanism,
            'water_resistant' : watch.water_resistant
        })
    return Response(data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    watch.delete()
    return Response({
        'msg' : 'Soat o`chirildi'
    }, status=200)   

@api_view(['PUT', 'PATCH'])
def update_watch(request, pk):
    try:
        watch = get_object_or_404(Watch, pk=pk)
        if 'water_resistant' in request.data:
            watch.water_resistant = request.data['water_resistant']
        if 'brand' in request.data:
            watch.brand = request.data['brand']
        if 'model' in request.data:
            watch.model = request.data['model']
        if 'description' in request.data:
            watch.description = request.data['description']
        if 'price' in request.data:
            watch.price = request.data['price']
        if 'screensize' in request.data:
            watch.screensize = request.data['screensize']
        if 'mechanism' in request.data:
            watch.mechanism = request.data['mechanism']
        watch.save()
        return Response({
            'msg' : 'Soat yangilandi'
        }, status=status.HTTP_200_OK)
    except NotFound:
        return Response({
            'msg' : 'Bunday id li soat topilmadi'
        }, status=status.HTTP_404_NOT_FOUND)































