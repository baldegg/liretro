from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'scoreboard'
urlpatterns = [
    path('', views.mainpage, name='index'),
    url(r'^achievementstation/day/(?P<day>\d+)/$', views.achievementcenter, name='achievementstation'),
    url(r'^tournament/day/(?P<day>\d+)/$', views.tournament, name='tournament'),
]