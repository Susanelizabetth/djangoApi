import email
from http import client
from lib2to3.pgen2 import driver
from uuid import uuid4
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http.request import HttpRequest
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from drf_yasg import openapi
from packages.models import Package
from .models import ChatRoom, Message, Order, Address
from .serializers import ChatRoomSerializer, MessageSerializer, SimpleOrderSerializer, OrderSerializer, AddressSerializer
# Create your views here.


class AddressView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING),
            "email": openapi.Schema(type=openapi.TYPE_STRING),
            "phone": openapi.Schema(type=openapi.TYPE_STRING),
            "dni": openapi.Schema(type=openapi.TYPE_STRING),
            "city": openapi.Schema(type=openapi.TYPE_STRING),
            "street": openapi.Schema(type=openapi.TYPE_STRING),
            "residence_number": openapi.Schema(type=openapi.TYPE_STRING), }))
    def post(self, request: HttpRequest) -> Response:
        address: Address = Address(
            name=request.data["name"],
            email=request.data["email"],
            phone=request.data["phone"],
            dni=request.data["dni"],
            city=request.data["city"],
            street=request.data["street"],
            residence_number=request.data["residence_number"],
            user=request.user
        )

        address.save()

        return Response(AddressSerializer(address).data)

    def get(self, request: HttpRequest) -> Response:
        return Response(AddressSerializer(Address.objects.all(), many=True).data)


class OrderView(APIView):

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "address_from": openapi.Schema(type=openapi.TYPE_INTEGER, description="address id"),
            "address_to": openapi.Schema(type=openapi.TYPE_INTEGER, description="address id"),
            "packages": openapi.Schema(type=openapi.TYPE_ARRAY,
                                       items=openapi.Items(
                                           type=openapi.TYPE_OBJECT,
                                           properties={
                                               "description": openapi.Schema(type=openapi.TYPE_STRING, description="package description"),
                                               "value": openapi.Schema(type=openapi.TYPE_NUMBER, description="package monetary value")
                                           }
                                       ),
                                       description="list of packages")
        }
    ))
    def post(self, request: HttpRequest) -> Response:
        order: Order = Order(
            user=request.user,
            address_from=Address.objects.get(pk=request.data["address_from"]),
            address_to=Address.objects.get(pk=request.data["address_to"])

        )
        order.save()

        for package in request.data["packages"]:
            package: Package = Package(
                description=package["description"], value=package["value"], order=order)
            package.save()

        return Response(SimpleOrderSerializer(order).data)

    def get(self, request: HttpRequest) -> Response:
        # if user is part of staff show all packages, if he isnt then only their packages
        orders = Order.objects.all() if request.user.is_staff else Order.objects.filter(
            user=request.user.id)
        return Response(SimpleOrderSerializer(orders, many=True).data)


class SingleOrderView(APIView):

    def get(self, request: HttpRequest, id: str) -> Response:
        return Response(OrderSerializer(Order.objects.get(pk=id)).data)


class MessageView(APIView):

    def get(self, request: HttpRequest) -> Response:

        chats = ChatRoom.objects.filter(
            Q(driver=request.user.pk) | Q(client=request.user.pk))

        return Response(ChatRoomSerializer(chats, many=True).data)


class MessagesView(APIView):

    def get(self, request: HttpRequest, room: str) -> Response:

        msgs = Message.objects.filter(room_chat=room)

        return Response(MessageSerializer(msgs, many=True).data)
