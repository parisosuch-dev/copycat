from django.http.request import HttpRequest
from rest_framework import permissions, status
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import Event
# from .serializers import EventSerializer


class EventAPIView(APIView):
    pass
