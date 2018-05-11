from django.shortcuts import render
from .models import Achievement, Score, Tournament
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def achievementcenter(request, day):
    n = 5
    if day == '0':
        games = Achievement.objects.all()
    elif day == '1':
        games = Achievement.objects.filter(event_time__day=11)
    elif day == '2':
        games = Achievement.objects.filter(event_time__day=12)
    achGames = []
    for game in games:
        title = game.game_or_event_name
        topN = game.score_set.all()[:n]
        game_id = game.pk
        # TODO fix this
        game_image = game.image.url[10:]
        game_time = game.event_time
        achGames.append({'game_id': game_id,
                         'title': title,
                         'image': game_image,
                         'time': game_time,
                         'topN': topN})

    context = {'achGames': achGames}

    return render(request, 'scoreboard/index.html', context)


def tournament(request, day):
    n = 5
    if day == '0':
        games = Tournament.objects.all()
    elif day == '1':
        games = Tournament.objects.filter(event_time__day=11)
    elif day == '2':
        games = Tournament.objects.filter(event_time__day=12)
    tourGames = []
    for game in games:
        title = game.game_name
        game_id = game.pk
        # TODO fix this
        game_image = game.image.url[10:]
        game_time = game.event_time
        first = game.first
        second = game.second
        third = game.third
        tourGames.append({'game_id': game_id,
                          'title': title,
                          'image': game_image,
                          'time': game_time,
                          'first': first,
                          'second': second,
                          'third': third})

    context = {'tourGames': tourGames}

    return render(request, 'scoreboard/index-tournament.html', context)


def achievement_detail(request, pk):
    game = get_object_or_404(Achievement, pk=pk)
    context = {'game': game}
    return render(request, 'scoreboard/gameboard.html', context)
