# Generated by Django 4.0.4 on 2022-04-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_parser', '0007_alter_configuration_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='name',
            field=models.CharField(default='textfile', max_length=100, verbose_name='Name'),
        ),
    ]
