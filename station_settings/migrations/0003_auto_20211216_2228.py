# Generated by Django 3.2.7 on 2021-12-16 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station_settings', '0002_auto_20211216_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='ChartSettings',
            new_name='chartsettings',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='DashboardSettings',
            new_name='dashboardsettings',
        ),
    ]
