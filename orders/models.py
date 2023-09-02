from django.db import models
from _api import settings
from uuid import uuid4
# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dni = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    residence_number = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='adresses', on_delete=models.CASCADE)

# crear modelo de estado del ordenes


class OrderState(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    value = models.CharField(
        max_length=100, unique=True, default="En espera")

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Order State'
        verbose_name_plural = 'Order States'

    def __str__(self):
        return f"{self.value}"

# creación del modelo de ordenes


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='order', on_delete=models.CASCADE)
    state = models.ForeignKey(
        OrderState, related_name="order", on_delete=models.CASCADE, default=1)
    address_from = models.ForeignKey(Address,
                                     related_name='orderfrom', on_delete=models.DO_NOTHING)
    address_to = models.ForeignKey(Address,
                                   related_name='orderto', on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.id}: {self.user}"

# crear modelo de chat room entre cliente y repartidor


class ChatRoom(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False)
    order = models.ForeignKey(
        Order, related_name='chat_room', on_delete=models.CASCADE)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='client_room', on_delete=models.CASCADE)
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='driver_room', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Chat Room'
        verbose_name_plural = 'Chat Rooms'

    def __str__(self):
        return f"{self.order}"

# crear modelo de mensajes en el chat room


class Message(models.Model):
    room_chat = models.ForeignKey(
        ChatRoom, related_name='message', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='message', on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"{self.user}: {self.message}"
