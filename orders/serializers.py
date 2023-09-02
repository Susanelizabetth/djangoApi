from rest_framework import serializers

from packages.serializers import PackageSerializer
from .models import ChatRoom, Message, Order, Address, OrderState
from _api.serializers import UserSerializer


class OrderStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderState
        fields = (
            "id", "value"

        )


class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = (
            "id",
            "name",
            "email",
            "phone",
            "dni",
            "city",
            "street",
            "residence_number",
            "user",

        )


class SimpleOrderSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    #packages = PackageSerializer(many=True)
    #address_from = AddressSerializer()
    #address_to = AddressSerializer()
    state = OrderStateSerializer()

    class Meta:
        model = Order
        fields = (
            "id",

            "state",
            "date_added",
            "packages"
        )


class OrderSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    packages = PackageSerializer(many=True)
    address_from = AddressSerializer()
    address_to = AddressSerializer()
    state = OrderStateSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "address_from",
            "address_to",
            "state",
            "date_added",
            "packages"
        )


class ChatRoomSerializer(serializers.ModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = ChatRoom
        fields = (
            "id",
            "order",
            "driver",
            "client",

        )


class MessageSerializer(serializers.ModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = Message
        fields = (

            "user",
            "message",
            "date_added",

        )
