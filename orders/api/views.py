from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


class OdersView(generics.GenericAPIView):
    def get(self, request):
        data = {
         'message' : 'all request'
        }
        return Response(data=data, status=status.HTTP_200_OK)
