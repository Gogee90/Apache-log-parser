from .serializers import ApacheLogSerializer
from rest_framework.generics import ListAPIView
from django.views.generic import ListView
from .models import ApacheLogs
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ApacheLogView(LoginRequiredMixin, ListView):
    model = ApacheLogs
    template_name = "log_parser/logs.html"
    login_url = "account/login/"

    def get_queryset(self):
        return self.model.filter_by(**self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["log"] = self.get_queryset
        return context


class ApacheLogAPIView(LoginRequiredMixin, ListAPIView):
    model = ApacheLogs
    serializer_class = ApacheLogSerializer
    login_url = "dj-rest-auth/login/"

    def get_queryset(self):
        return self.model.filter_by(**self.request.GET)
