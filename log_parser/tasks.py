from celery import shared_task
from .models import ApacheLogs, Configuration, CeleryLogs
from apachelogs import LogParser
from django.core.files import File
from datetime import date


@shared_task
def aggregate_logs():
    try:
        parser = LogParser('%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i"')
        config = Configuration.objects.filter(name="access_log").first()
        access_log = open(config.access_log_path, "r")
        generated_file = File(access_log)
        config.file_path.save(f"{config.name}.txt", generated_file)
        access_log.close()
        with open(config.file_path.path) as fp:
            for entry in parser.parse_lines(fp):
                if entry.request_time == date.today():
                    ApacheLogs.objects.get_or_create(
                        bytes_sent=entry.bytes_sent,
                        referer=entry.headers_in["Referer"],
                        user_agent=entry.headers_in["User-Agent"],
                        remote_host=entry.remote_host,
                        remote_logname=entry.remote_logname,
                        remote_user=entry.remote_user,
                        request_line=entry.request_line,
                        final_status=entry.final_status,
                        request_time=entry.request_time,
                    )
    except Exception as error:
        CeleryLogs.objects.create(name="aggregate logs", message=str(error))
