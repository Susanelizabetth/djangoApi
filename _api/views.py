from rest_framework.views import APIView

# from django.http import Http404,HttpResponseBadRequest,HttpResponseNotFound
# from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from rest_framework import serializers,parsers

from rest_framework.permissions import IsAuthenticated
import rest_framework.permissions


class verify_token(APIView):
    def get(self, request):
        return Response({"detail": "authorized"})


@api_view(["GET"])
@permission_classes([AllowAny])
def healthcheck( request):
    return Response({"status": "healthy"})
