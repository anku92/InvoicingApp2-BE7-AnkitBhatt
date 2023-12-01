from rest_framework import serializers
from .models import UserModel, InvoiceModel, ItemModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        exclude = ("invoice",)


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = InvoiceModel
        fields = "__all__"
