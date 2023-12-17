from django.urls import include, path

from .views.project_view import ProjectAPIView
from .views.channel_view import ChannelAPIView
from .views.event_view import EventAPIView, ProjectEventsView, ProjectChannelEventsView

urlpatterns = [
    path("project/", ProjectAPIView.as_view()),
    path("channel/", ChannelAPIView.as_view()),
    path("log/", EventAPIView.as_view()),
    path("log/<str:project>/", ProjectEventsView.as_view()),
    path("log/<str:project>/<str:channel>/", ProjectChannelEventsView.as_view()),
]
