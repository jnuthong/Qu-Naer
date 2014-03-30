
from utils.user_functions import ajax_login_required
from django.views.decorators.http import *
from utils.json_functions import json_view
from django.shortcuts import HttpResponse
from apps.user_third import views as third_views
from apps.user import views as user_views
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie

@require_POST
@json_view
def login(request):
    """
    User login
    """
    return user_views.login(request)

@require_POST
@json_view
@csrf_protect
def register(request):
    """
    """
    return user_views.register(request)

@require_POST
@json_view
@ajax_login_required
def logout(request):
    """
    User logout
    @param request:
    @return:
    """
    return user_views.logout(request)

@require_POST
@json_view
@ajax_login_required
def get_user_info(request):

    """
    Get user info
    @param request:
    @return:
    """
    # return user_views.get_user_info(request)
    pass

@require_POST
@json_view
@ajax_login_required
def update_user_info(request):

    """
    Update user info
    @param request:
    @return:
    """
    return user_views.update_user_info(request)

@require_POST
@json_view
def check_third_user_is_exist(request):

    """
    Check if the third user is exist, and register third user
    @param request:
    @return:
    """
    return third_views.check_third_user_is_exist(request)

@require_POST
@json_view
def update_third_user_info(request):

    """
    Update the third user info
    @param request:
    @return:
    """
    return third_views.update_third_user_info(request)

@require_POST
@json_view
def third_user_login(request):

    """
    Login for third user
    @param request:
    @return:
    """
    return third_views.third_user_login(request)

@ensure_csrf_cookie
def get_test_csrf(request):
    """
    Normal get test to get csrf token
    """
    return HttpResponse('Hello world')
