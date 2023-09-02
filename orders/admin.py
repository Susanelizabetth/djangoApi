from django.contrib import admin

# Register your models here.
from .models import Order

from .models import OrderState
from .models import ChatRoom
from .models import Message
from .models import Address


@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "user", 'email', 'dni', "city", "street")
    search_fields = ('id', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',  'address_from',
                    'address_to', 'date_added')
    search_fields = ('id', 'user')
    list_editable = ('address_from', 'address_to')


@admin.register(OrderState)
class OrderStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ('id', 'value')
    list_editable = ('value',)


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'client', 'driver')
    search_fields = ('id', 'order', 'client', 'driver')
    list_editable = ('client', 'driver')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room_chat', 'user', 'message', 'date_added')
    search_fields = ('room_chat', 'user', 'message')
    list_editable = ('message',)
