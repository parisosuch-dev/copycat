from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Channel, Event, Project
from .serializers import ChannelSerializer, EventSerializer, ProjectSerializer


class ProjectAPIView(APIView):
    pass


class ChannelAPIView(APIView):
    pass


class EventAPIView(APIView):
    pass
