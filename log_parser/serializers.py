from rest_framework.serializers import ModelSerializer
from .models import ApacheLogs


class ApacheLogSerializer(ModelSerializer):
    class Meta:
        model = ApacheLogs
        fields = "__all__"
