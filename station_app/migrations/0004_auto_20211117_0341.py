# Generated by Django 3.2.7 on 2021-11-17 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0003_auto_20211117_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='edit',
        ),
        migrations.RemoveField(
            model_name='station',
            name='edit',
        ),
    ]
