# Generated by Django 3.2.7 on 2021-10-08 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='station',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]