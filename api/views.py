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

    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        """Post project for user

        Args:
            request (HttpRequest): incoming http request

        Returns:
            Response: http status code
        """
        data = {
            "name": request.data.get("name"),
            "user": request.user.id,
        }
        # serialize and validate data
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChannelAPIView(APIView):
    pass


class EventAPIView(APIView):
    pass
