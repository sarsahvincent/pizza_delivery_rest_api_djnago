from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializsers
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    # routes = [
    #     '/api/token',
    #     '/api/token/refresh',
    # ]
    routes = [
        '/login',
        '/token/refresh',
    ]
    return Response(routes)


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        data = {
            'message': 'Hello Atuh',
        }
        return Response(data=data, status=status.HTTP_200_OK)


class CreateUserView(generics.GenericAPIView):
    serializer_class = serializsers.UserCreationSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
