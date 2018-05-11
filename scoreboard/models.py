from django.db import models


class Achievement(models.Model):
    class Meta:
        verbose_name = "Achievement Station Game"
        ordering = ['event_time']
    image = models.ImageField(upload_to='scoreboard/static/scoreboard/images/achgames')
    game_or_event_name = models.CharField(max_length=200, unique=True)
    event_time = models.DateTimeField("Scheduled Date/Time", blank=True)
    def __str__(self):
        return self.game_or_event_name

class Player(models.Model):
    player_name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.player_name

class Tournament(models.Model):
    class Meta:
        verbose_name = "Tournament Game"
        ordering = ['event_time']
    game_name = models.CharField(max_length=200, unique=True)
    event_time = models.DateTimeField("Scheduled Date/Time", blank=True)
    image = models.ImageField(upload_to='scoreboard/static/scoreboard/images/tourgames')
    first = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='first+', verbose_name="First Place Player/Team", blank = True, null=True)
    second = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='second+', verbose_name="Second Place Player/Team", blank = True, null=True)
    third = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='third+', verbose_name="Third Place Player/Team", blank = True, null=True)

    def __str__(self):
        return self.game_name


class Score(models.Model):
    class Meta:
        verbose_name = "Achievement Station Score"
        ordering = ['-score', 'time']
    score = models.IntegerField("Score - leave blank if time achievement", blank = True, null=True)
    time = models.TextField("Time - leave blank if high score achievement", blank=True, null=True, max_length=20)
    game_or_event = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    def __str__(self):
        return self.game_or_event.game_or_event_name + " - " + self.player.player_name + " - " + (str(self.time) if self.time else str(self.score))
