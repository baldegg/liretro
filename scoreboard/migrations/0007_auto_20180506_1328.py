# Generated by Django 2.0.5 on 2018-05-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0006_auto_20180506_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='event_time',
            field=models.DateTimeField(blank=True, verbose_name='Scheduled Date/Time'),
        ),
    ]
