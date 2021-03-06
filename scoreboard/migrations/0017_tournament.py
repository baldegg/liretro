# Generated by Django 2.0.5 on 2018-05-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0016_auto_20180507_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='scoreboard/static/scoreboard/images/tourgames')),
                ('game_name', models.CharField(max_length=200, unique=True)),
                ('event_time', models.DateTimeField(blank=True, verbose_name='Scheduled Date/Time')),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first+', to='scoreboard.Player')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second+', to='scoreboard.Player')),
                ('third', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third+', to='scoreboard.Player')),
            ],
            options={
                'verbose_name': 'Tournament Game',
                'ordering': ['event_time'],
            },
        ),
    ]
