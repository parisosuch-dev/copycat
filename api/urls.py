from django.urls import include, path

from .views import ProjectAPIView

urlpatterns = [
    path("project/", ProjectAPIView.as_view()),
]
