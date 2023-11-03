from rest_framework import serializers
from .models import Project, Channel, Event


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "created_at"]


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["project_id", "name", "created_at"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["project_id", "channel_id", "event_name", "description", "icon", "created_at"]
