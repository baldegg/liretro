# Generated by Django 2.0.5 on 2018-05-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0019_auto_20180508_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='image',
            field=models.ImageField(upload_to='scoreboard/static/scoreboard/images/achgames'),
        ),
    ]