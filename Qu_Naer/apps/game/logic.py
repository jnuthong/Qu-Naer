#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '12/09/2015'

from utils.logger import error
from apps.game.models import Game,Company,Type,GameType,Platform,GamePlatform


class GameLogic(object):
    @classmethod
    def get_one_game(cls, game_id):
        game_dict = Game.get_one_game(game_id).canonical()
        return game_dict

    @classmethod
    def get_game_list(cls, page_num):
        try:
            print "logic begin:"
            if(page_num<1):
                raise Exception(u'FUCK!PAGENUM<1!')
            game_id_list = Game.get_game_list(page_num)
            print game_id_list
            game_dict_list = []
            if len(game_id_list) > 0:
                for game_id in game_id_list:
                    game_dict_list.append(Game.get_one_game(game_id).canonical_trim_game())
                return game_dict_list
            else:
                return []
        except Exception as e:
            print e
            return []

    @classmethod
    def get_total_num(cls):
        return Game.get_total_num()

    @classmethod
    def create_game(cls, **kwargs):
        try:
            game = Game.create_game(**kwargs)
            return game.canonical()
        except Exception as e:
            print('create_game failed:%s' % str(e))
            return None

    @classmethod
    def get_company_id(cls, company_name):
        company_id = Company.get_company_by_name(company_name).comp_id
        return company_id

    @classmethod
    def update_game(cls, **kwargs):
        """
        Update game property base on the argument game_id
        """
        try:
            game_id = kwargs.pop('game_id')
            game = Game.get_one_game(game_id)
            if game and game.user_id == int(kwargs.pop('user_id')):
                for key, value in kwargs.items():
                    setattr(game, key, value)
                game.save()
                return game.canonical()
            else:
                raise Exception("No exist Game:game_id: %s" %game_id)
        except Exception as e:
            print(e)
            return 0

    @classmethod
    def delete_game(cls, game_id, user_id):
        game = Game.objects.get(game_id=game_id)
        if game is None:
            raise Exception(u'game_id is not exist')
        if user_id != game.user_id:
            raise Exception(u'not your game')
        game.game_status = 1
        game.save()
        return



