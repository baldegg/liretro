from django.contrib import admin
from .models import Score, Achievement, Player, Tournament
# Register your models here.
admin.site.register(Score)
admin.site.register(Achievement)
admin.site.register(Player)
admin.site.register(Tournament)

