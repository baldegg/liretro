# Generated by Django 2.0.5 on 2018-05-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0011_auto_20180506_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='image',
            field=models.ImageField(upload_to='scoreboard/static/images/achgames'),
        ),
    ]
