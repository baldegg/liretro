from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'scoreboard'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^day/(?P<pk>\d+)/$', views.index, name='index'),
    url(r'^event/(?P<pk>\d+)/$', views.achievement_detail, name='post_detail'),
]