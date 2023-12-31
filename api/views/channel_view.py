from rest_framework.request import Request
from rest_framework import permissions, status
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Channel
from ..serializers import ChannelSerializer


class ChannelAPIView(APIView):
    # check if user is auth
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """Get all channels for a user

        Args:
            request (Request): incoming http request

        Returns:
            Response: user channels serialized in json
        """
        channels = Channel.objects.filter(user=request.user.id)
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs) -> Response:
        """Post channel for user

        Args:
            request (Request): incoming http request

        Returns:
            Response: http status code
        """
        # check if channel name already exists for user in project
        channels = Channel.objects.filter(
            user=request.user.id,
            name=request.data.get("name"),
            project_id=request.data.get("project_id"),
        )
        if len(channels) > 0:
            return Response(
                {"message": "Channel name already exists for project."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "project_id": request.data.get("project_id"),
            "name": request.data.get("name"),
            "user": request.user.id,
        }
        # serialize and validate data
        serializer = ChannelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
