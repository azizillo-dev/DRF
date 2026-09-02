from rest_framework.views import APIView
from .serializers import *
from .models import CustomUSer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .permissions import IsLoggedIn
from rest_framework.authtoken.models import Token

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "msg" : "Registered",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)


class SignInView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request=request, username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        if user is None:
            return Response({
                "msg" : "Login yoki parol xato"
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({
            "msg" : "Logged in",
            "user" : {
                "id" : user.id,
                "username" : user.username
            },
            "token" : token.key
        }, status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [IsLoggedIn, ]
    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response({
            "msg" : "Profile",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)

    
class ProfileUpdateView(APIView):
    permission_classes = [IsLoggedIn, ]
    def patch(self, request):
        serializer = ProfileUpdateSerializer(data=request.data, instance=request.user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "msg" : "Profile updatet",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)


class PasswordUpdateView(APIView):
    permission_classes = [IsLoggedIn, ]
    def put(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')

        cr_user = authenticate(username=request.user.username, password=old_password)
        if cr_user is None:
            return Response({
                "msg" : "Eski parol noto'g'ri"
            }, status=status.HTTP_400_BAD_REQUEST)
        cr_user.set_password(new_password)
        cr_user.save()
        return Response({
            "msg" : "Password updated !"
        })


class LogoutView(APIView):
    permission_classes = [IsLoggedIn, ]
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({
            "msg" : "Tizimdan chiqdingiz!"
        }, status=status.HTTP_200_OK)
    1   