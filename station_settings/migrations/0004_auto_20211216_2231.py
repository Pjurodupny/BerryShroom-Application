# Generated by Django 3.2.7 on 2021-12-16 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station_settings', '0003_auto_20211216_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='chartsettings',
            new_name='chart_settings',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='dashboardsettings',
            new_name='dashboard_settings',
        ),
    ]
