from django.urls import path
from .views import OrderView, AddressView, SingleOrderView, MessageView, MessagesView
urlpatterns = [

    path("", OrderView.as_view()),

    path("/chats", MessageView.as_view()),
    path("/chats/<str:room>", MessagesView.as_view()),
    path("/<str:id>", SingleOrderView.as_view()),
    path("/addresses", AddressView.as_view()),

]
