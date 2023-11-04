"""
Copy Cat Log Models
===================

Project
-------
id*
name*
create_at* (autogen)
user

Channel
-------
id*
project_id*
name*
created_at* (autogen)
user

Event
-----
project_id*
channel_id*
event_name*
description
icon
created_at (autogen)
user
"""
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Channel(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    event_name = models.TextField()
    description = models.TextField(null=True)
    icon = models.CharField(max_length=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
