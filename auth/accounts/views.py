from django.shortcuts import render
from .serializers import SignUpSerializer,CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response



class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)




