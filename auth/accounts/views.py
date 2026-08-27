from django.shortcuts import render
from .serializers import SignUpSerializer,ProfileSerializer, ProfileUpdateSerializer, PasswordChangeSerializer
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data.pop('conf_pass')
        user = CustomUser.objects.create_user(**serializer.validated_data)

        return Response(SignUpSerializer(user).data)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')


        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError(detail='Parol yoki username xato')

        
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'msg':'Login',
            'token': token.key
        }, status=status.HTTP_200_OK)
    


class ProfileView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)
        return Response({'msg': 'me', 'data': serializer.data}, status=status.HTTP_200_OK)

    

class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        serializer = ProfileUpdateSerializer(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': 'Profile updated',
            'data': serializer.data,
        }, status=status.HTTP_200_OK)



class PassChangeView(APIView):
    permission_classes = [IsAuthenticated, ]
    def put(self, request):
        user = request.user
        serializer = PasswordChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        current_user = authenticate(username=user.username, password=serializer.validated_data['old_password'])
        if current_user is None:
            raise ValidationError(detail='eski parol xato')

        current_user.set_password(serializer.validated_data['new_password'])
        current_user.save()

        return Response({
            'msg':'Password updated',
            
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        Token.objects.filter(user=request.user).delete()

        return Response({
            'msg': 'Tizimdan chiqdingiz'
        }, status=status.HTTP_200_OK)

    
