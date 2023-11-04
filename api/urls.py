from django.urls import include, path

from .views import ProjectAPIView

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("project/", ProjectAPIView.as_view()),
]
