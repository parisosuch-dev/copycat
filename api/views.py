from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http.request import HttpRequest
from .models import Channel, Event, Project
from .serializers import ChannelSerializer, EventSerializer, ProjectSerializer


class ProjectAPIView(APIView):
    # check if user is auth
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        """Get all projects for user

        Args:
            request (HttpRequest): incoming http request

        Returns:
            Response: user projects serialized in json
        """
        projects = Project.objects.filter(user=request.user.id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChannelAPIView(APIView):
    pass


class EventAPIView(APIView):
    pass
