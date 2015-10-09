#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '12/09/2015'


from django.conf.urls import *
from apps.game import views
import apps.game.views

urlpatterns = patterns('',
    url(r'^get_one_game', apps.game.views.get_one_game, name='get_one_game'),
    url(r'^create_game', apps.game.views.create_game, name='create_game'),
    url(r'^get_game_list', apps.game.views.get_game_list, name='get_game_list')
    # url(r'^delete_game', apps.game.views.delete_game, name='delete_game')
)
