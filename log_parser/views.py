from .serializers import ApacheLogSerializer
from rest_framework.generics import ListAPIView
from django.views.generic import ListView
from .models import ApacheLogs
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ApacheLogView(LoginRequiredMixin, ListView):
    model = ApacheLogs
    template_name = "log_parser/logs.html"
    login_url = 'account/login/'

    def get_queryset(self):
        queryset = ApacheLogs.objects.all()
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        ip_address = self.request.GET.get("ip_address")

        if start_date:
            queryset = queryset.filter(request_time__gte=start_date)

        if end_date:
            queryset = queryset.filter(request_time__lte=end_date)

        if start_date and end_date:
            queryset = queryset.filter(
                request_time__gte=start_date, request_time__lte=end_date
            )

        if ip_address:
            queryset = queryset.filter(remote_host=ip_address)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["log"] = self.get_queryset
        return context


class ApacheLogAPIView(LoginRequiredMixin, ListAPIView):
    serializer_class = ApacheLogSerializer
    login_url = 'dj-rest-auth/login/'
    
    def get_queryset(self):
        queryset = ApacheLogs.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        ip_address = self.request.query_params.get('ip_address')
        
        if start_date:
            queryset = queryset.filter(request_time__gte=start_date)

        if end_date:
            queryset = queryset.filter(request_time__lte=end_date)

        if start_date and end_date:
            queryset = queryset.filter(
                request_time__gte=start_date, request_time__lte=end_date
            )
        
        if ip_address:
            queryset = queryset.filter(remote_host=ip_address)
            
        return queryset
        
