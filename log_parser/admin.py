from django.contrib import admin
from .models import ApacheLogs, Configuration, CeleryLogs


class ApacheLogsAdmin(admin.ModelAdmin):
    list_display = ('remote_host', 'request_time', 'final_status')
    search_fields = ['remote_host', 'final_status']

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('name', 'access_log_path')
    search_fields = ['name']
    
class CeleryLogsAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ['name']

# Register your models here.
admin.site.register(ApacheLogs, ApacheLogsAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(CeleryLogs, CeleryLogsAdmin)
