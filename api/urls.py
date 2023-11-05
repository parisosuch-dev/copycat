from django.urls import include, path

from .views import ProjectAPIView, ChannelAPIView

urlpatterns = [
    path("project/", ProjectAPIView.as_view()),
    path("channel/", ChannelAPIView.as_view()),
]
