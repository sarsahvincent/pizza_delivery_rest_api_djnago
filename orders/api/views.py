from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializsers
from orders.models import Order
from rest_framework.permissions import IsAuthenticated


class OrderCreateListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializsers.OderCreationSerializer
    queryset = Order.objects.all()

    def get(self, request):
        user = request.user

        # get all orders
        orders = Order.objects.all()

        # get oders for logged in users
        # orders = user.order_set.all()

        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        user = request.user
        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetriewveUpdateDeleteOrder(generics.GenericAPIView):
    serializer_class = serializsers.OderDetailSerializer

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)

        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        data = request.data

        order = get_object_or_404(Order, pk=order_id)

        serializer = self.serializer_class(instance=order, data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):

        order = get_object_or_404(Order, pk=order_id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateOrderStatus(generics.GenericAPIView):

    serializer_class = serializsers.UpdateOrderStatus

    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data

        serializer = self.serializer_class(instance=order, data=data)
        # serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOdersView(generics.GenericAPIView):
    serializer_class = serializsers.OderDetailSerializer

    def get(self, request):
        user = request.user
        # orders = user.order_set.all()
        orders = Order.objects.all().filter(customer=user)

        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
