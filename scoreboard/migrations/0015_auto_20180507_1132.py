# Generated by Django 2.0.5 on 2018-05-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0014_auto_20180507_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='image',
            field=models.ImageField(upload_to='static/scoreboard/images/achgames'),
        ),
    ]
