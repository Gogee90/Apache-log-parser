# Generated by Django 4.0.4 on 2022-04-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_parser', '0002_configuration'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='file_path',
            field=models.FileField(blank=True, default=None, null=True, upload_to='media', verbose_name='File Path'),
        ),
    ]
