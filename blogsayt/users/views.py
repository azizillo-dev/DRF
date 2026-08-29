from rest_framework.views import APIView
from .serializers import SignUpSerializer
from .models import CustomUSer
from rest_framework.response import Response
from rest_framework import status

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "msg" : "Registered",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)
    