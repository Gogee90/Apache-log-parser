from attr import fields
from django_filters import rest_framework as filters
from .models import ApacheLogs


class ApacheLogsFilter(filters.FilterSet):
    request_time = filters.DateFromToRangeFilter()

    class Meta:
        model = ApacheLogs
        fields = ("request_time", "remote_host")
