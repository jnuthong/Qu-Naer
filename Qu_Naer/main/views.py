# -*- encoding: utf-8 -*-
# Author: J
# Here is some code stardard written by J
#   1. root directory is main/;
#   2. root view only could import view from mapi layer;
#   3. module in apps, should not allow to import another module outside apps; exception utils/

from django.shortcuts import render

from mapi.views import *

def views_validEmail(request):
    """
    Check a given email is alread existed in system or not;
    if yes, return 1, else return 0
    """
    return validEmail(request)

def views_signup(request):
    """
    """
    return signup(request)

def views_test(request):
    """
    """
    # return render(request, "info_temp.html",{})
    return render(request, "j_blog/article.html", {'title': "Machine Learning Thing in this article!",
                                                   'author': "Jianbin, Hong",
                                                   'create_date': '2015-04-10'})

def views_signin(request):
    """
    """
    return render(request, "signin.html", {})

def activeAccount(request):
    """
    """
    return active_account(request)