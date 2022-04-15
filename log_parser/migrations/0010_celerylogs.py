# Generated by Django 4.0.4 on 2022-04-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_parser', '0009_apachelogs_referer_apachelogs_user_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Task Name')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]