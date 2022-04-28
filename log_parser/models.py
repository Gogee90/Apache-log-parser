from django.db import models


# Create your models here.
class Configuration(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", default="textfile")
    access_log_path = models.CharField(
        verbose_name="Access Log Path", max_length=255, null=True, blank=True
    )
    file_path = models.FileField(
        verbose_name="File Path", upload_to="media", default=None, null=True, blank=True
    )

    verbose_name = "Configuration"
    verbose_name_plural = "Configurations"

    def __str__(self):
        return f"{self.access_log_path}"


class ApacheLogs(models.Model):
    bytes_sent = models.IntegerField(verbose_name="Bytes Sent", blank=True, null=True)
    referer = models.CharField(
        verbose_name="Referer", max_length=255, blank=True, null=True
    )
    user_agent = models.CharField(
        verbose_name="User Agent", max_length=255, null=True, blank=True
    )
    remote_host = models.CharField(
        verbose_name="Remote Host", max_length=255, blank=True, null=True
    )
    remote_logname = models.CharField(
        verbose_name="Remote Log Name", max_length=255, blank=True, null=True
    )
    remote_user = models.CharField(
        verbose_name="Remote User", max_length=255, blank=True, null=True
    )
    request_line = models.CharField(
        verbose_name="Request Line", max_length=255, blank=True, null=True
    )
    final_status = models.CharField(
        verbose_name="Final Status", max_length=255, blank=True, null=True
    )
    request_time = models.DateTimeField(
        verbose_name="Request Time", blank=True, null=True
    )

    verbose_name = "Apache Log"
    verbose_name_plural = "Apache Logs"

    def __str__(self):
        return f"{self.remote_host} {self.request_time} {self.final_status}"

    @classmethod
    def filter_by(cls, **kwargs):
        queryset = cls.objects.all()
        if kwargs:
            start_date, end_date, ip_address = kwargs.values()
            if start_date[0]:
                queryset = queryset.filter(request_time__lte=start_date[0])
            if end_date[0]:
                queryset = queryset.filter(request_time__gte=end_date[0])
            if ip_address[0]:
                queryset = queryset.filter(remote_host=ip_address[0])
        return queryset


class CeleryLogs(models.Model):
    name = models.CharField(
        verbose_name="Task Name", max_length=100, blank=True, null=True
    )
    message = models.TextField(verbose_name="Message", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    verbose_name = "Celery Log"
    verbose_name_plural = "Celery Logs"
