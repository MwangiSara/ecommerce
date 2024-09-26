from rest_framework import serializers
from rest_framework import status
from rest_framework.validators import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from .models import Customer,Item, Order, OrderDetail



class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=100)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)
    password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = Customer
        fields = ["username", "email", "phone_number", "password"]

    # create custom validation for email, username

    def validate(self, attrs):
        email = Customer.objects.filter(email=attrs["email"]).exists()
        if email:
            raise ValidationError(
                {"success": False, "message": "Email already exists"},
                code=status.HTTP_403_FORBIDDEN,
            )

        username = Customer.objects.filter(username=attrs["username"]).exists()
        if username:
            raise ValidationError(
                {"success": False, "message": "Username already exists"},
                code=status.HTTP_403_FORBIDDEN,
            )

        phone_number = Customer.objects.filter(
            phone_number=attrs["phone_number"]
        ).exists()
        if phone_number:
            raise ValidationError(
                {"success": False, "message": "Phone number already exists"},
                code=status.HTTP_403_FORBIDDEN,
            )

        return super().validate(attrs)

    def create(self, validated_data):
        new_user = Customer(**validated_data)

        new_user.password = make_password(validated_data.get("password"))

        new_user.save()

        return new_user

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["id"]


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"
        read_only_fields = ["id"]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ["id"]
