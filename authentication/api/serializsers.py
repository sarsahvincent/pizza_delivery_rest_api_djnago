from operator import mod
from authentication.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=25, )
    email = serializers.EmailField(max_length=80, )
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs.get('username')).exists()

        if username_exists:
            raise serializers.ValidationError(detail='Username already exists')

        email_exists = User.objects.filter(email=attrs.get('email')).exists()

        if email_exists:
            raise serializers.ValidationError(detail='email already exists')

        phonenumber_exists = User.objects.filter(phone_number=attrs.get('phone_number')).exists()

        if phonenumber_exists:
            raise serializers.ValidationError(detail='phone number already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user
