from django.urls import path
from .views import ApacheLogView, ApacheLogAPIView

urlpatterns = [
    path("", ApacheLogView.as_view(), name="logs-list"),
    path("api/", ApacheLogAPIView.as_view(), name="api-logs-list"),
]
