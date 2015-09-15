#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '12/09/2015'

from apps.game.logic import GameLogic
from main.settings import DEBUG


def create_game(request):
    """
    create game
    """
    try:
        if request.method == "POST" or DEBUG is True:
            developer_name = request.POST.get('developer_name')
            publisher_name = request.POST.get('publisher_name')
            developer_id = GameLogic.get_company_id(developer_name)
            publisher_id = GameLogic.get_company_id(publisher_name)

            game_name = request.POST.get('game_name')
            game_alias = request.POST.get('game_alias','')
            initial_name = request.POST.get('initial_name','')
            release_date = request.POST.get('release_date','')
            game_language = request.POST.get('game_language','')
            game_brief = request.POST.get('game_brief','')
            game_space = request.POST.get('game_space','')
            game_site = request.POST.get('game_site','')
            game_level = request.POST.get('game_level','')

            #cover_image = request.POST.get('cover_image')   

            ret = GameLogic.create_game(game_name, game_alias, initial_name, developer_id,
                                         publisher_id, release_date, game_brief, game_language, 
                                         game_space, game_level, game_site)
            if ret is None:
                raise Exception(u'create failed')
            ret = dict(code=1, content=ret)
        else:
            ret = dict(code=2002, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        import traceback
        traceback.print_exc()
        ret = dict(code=2002, msg=u"Internal error:%s" % str(e))
    return ret

def get_one_game(request):
    """
    get the game according to game_id
    """
    try:
        if request.method == "POST" or DEBUG is True:
            game_id = request.POST.get('game_id')
            if game_id is None:
                raise Exception('parameter error')
            game_dict = GameLogic.get_one_game(game_id=game_id)
            if game_dict is None:
                raise Exception(u'game_id not exist')
            ret = dict(code=1, content=game_dict)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret

def get_game_list(request):
    """
    get game list
    """
    try:
        if request.method == "POST" or DEBUG is True:
            page_num = request.POST.get('page_num')
            game_dict_list = GameLogic.get_game_list(page_num)
            ret = dict(code=1, content=game_dict_list)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret



