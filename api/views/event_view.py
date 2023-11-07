from rest_framework.request import Request
from rest_framework import permissions, status
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Channel, Event, Project
from ..serializers import EventSerializer, ChannelSerializer


class EventAPIView(APIView):
    # check if user is auth
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """Get all events for a user

        Args:
            request (HttpRequest): incoming http request

        Returns:
            Response: user channels serialized in json
        """
        events = Event.objects.filter(user=request.user.id)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs) -> Response:
        """Post a log

        Args:
            request (HttpRequest): incoming http request

        Returns:
            Response: http status code
        """
        # if any of the required field are empty
        if (
            request.data.get("project") is None
            or request.data.get("channel") is None
            or request.data.get("event") is None
        ):
            return Response({"message": "Required fields are empty."})
        # if the project does not exist for user, throw err
        projects = Project.objects.filter(
            user=request.user.id, name=request.data.get("project")
        )
        if len(projects) == 0:
            return Response(
                {"message": "Project does not exist for user."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # get project id from projects query
        project_id = projects.values("id")[0]["id"]

        # if the channel does not exist, create the channel
        channels = Channel.objects.filter(
            user=request.user.id, name=request.data.get("channel")
        )
        if len(channels) == 0:
            channel_data = {
                "project_id": project_id,
                "name": request.data.get("channel"),
                "user": request.user.id,
            }
            channel_serializer = ChannelSerializer(data=channel_data)
            if not channel_serializer.is_valid():
                return Response(
                    {
                        "message": "Server error when saving new channel.",
                        "serializer_errors": channel_serializer.errors,
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            channel_serializer.save()
        channel_id = Channel.objects.filter(
            user=request.user.id, name=request.data.get("channel")
        ).values("id")[0]["id"]

        # post log to db
        data = {
            "project_id": project_id,
            "channel_id": channel_id,
            "event_name": request.data.get("event"),
            "description": request.data.get("description"),
            "icon": request.data.get("icon"),
            "user": request.user.id,
        }
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
