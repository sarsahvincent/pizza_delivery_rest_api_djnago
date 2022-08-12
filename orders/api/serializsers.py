from operator import mod
from pyexpat import model
from orders.models import Order
from rest_framework import serializers


class OderCreationSerializer(serializers.ModelSerializer):

    class Meta:
        size = serializers.CharField(max_length=20)
        order_status = serializers.CharField(max_length=20, default='PENDING')
        quantity = serializers.IntegerField()
        model = Order
        fields = ['id', 'size', 'order_status', 'quantity', 'customer']


class OderDetailSerializer(serializers.ModelSerializer):
    class Meta:

        size = serializers.CharField(max_length=20)
        order_status = serializers.CharField(max_length=20, default='PENDING')
        quantity = serializers.IntegerField()
        quantity = serializers.IntegerField()
        created_at = serializers.DateTimeField()
        updated_at = serializers.DateTimeField()

        model = Order
        fields = ['size', 'order_status', 'quantity', 'created_at', 'updated_at', 'customer']


class UpdateOrderStatus(serializers.ModelSerializer):

    order_status = serializers.CharField(max_length=20, default='PENDING')

    class Meta:
        model = Order
        fields = ['order_status']
