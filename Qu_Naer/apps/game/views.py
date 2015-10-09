#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '12/09/2015'

from apps.game.logic import GameLogic
from utils.json_functions import json_view
from main.settings import DEBUG
from django.shortcuts import render

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

@json_view
def get_one_game_json(request):
    """
    get the game according to game_id
    """
    try:
        print 'view get_one_game'
        if request.method == "GET" or DEBUG is True:
            game_id = request.GET.get('game_id')
            print('view get_one_game,%s' % game_id)
            if game_id is None:
                raise Exception('parameter error')
            game_dict = GameLogic.get_one_game(int(game_id))
            if game_dict is None:
                raise Exception(u'game_id not exist')
            ret = dict(code=1, content=game_dict)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret

def get_one_game(request):
    """
    get the game according to game_id
    """
    try:
        print 'view get_one_game'
        if request.method == "GET" or DEBUG is True:
            game_id = request.GET.get('game_id')
            print('view get_one_game,%s' % game_id)
            if game_id is None:
                raise Exception('parameter error')
            game_dict = GameLogic.get_one_game(int(game_id))
            if game_dict is None:
                raise Exception(u'game_id not exist')
            print game_dict
            ret = render(request, "gplat/gamedetail.html", game_dict)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        print str(e)
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret

def get_game_list(request):
    """
    get game list
    """
    try:
        if request.method == "GET" or DEBUG is True:
            page_num = request.GET.get('page_num')
            game_dict_list = GameLogic.get_game_list(int(page_num))
            ret_dict = dict(game_list=game_dict_list)
            
            if int(page_num) <= 1:
                ret_dict["prepageno"] = 1
            else:
                ret_dict["prepageno"] = int(page_num) - 1

            ret_dict["nextpageno"] = int(page_num) + 1

            ret_dict['total_num']=GameLogic.get_total_num()
            print "ret_dict", ret_dict
            ret = render(request, 'gplat/homepage.html', ret_dict)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret

@json_view
def get_game_list_json(request):
    """
    get game list
    """
    try:
        if request.method == "GET" or DEBUG is True:
            page_num = request.GET.get('page_num')
            game_dict_list = GameLogic.get_game_list(int(page_num))
            ret_dict = dict(game_list=game_dict_list)
            ret_dict['total_num']=GameLogic.get_total_num()
            ret = dict(code=1, content=ret_dict)
        else:
            ret = dict(code=2001, msg=u"Invalid method. Use POST. You used %s" % request.method)
    except Exception as e:
        ret = dict(code=2001, msg=u"Internal error: %s" % str(e))
    return ret

