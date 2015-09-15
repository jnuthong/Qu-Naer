from utils.user_functions import ajax_login_required
from django.views.decorators.http import *
from utils.json_functions import json_view, http_json_wraper, info_wraper
from apps.user_third import views as third_views
from apps.profile import views as profile_views
# from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie, requires_csrf_token

@ensure_csrf_cookie
@requires_csrf_token
@http_json_wraper
def validEmail(request):
    """
    """
    return profile_views.validEmail(request)

@http_json_wraper
def active_account(request):
    """
    """
    return profile_views.activeAccount(request)

@ensure_csrf_cookie
def signup(request):
    """
    User sign up
    """
    return profile_views.signup(request)

@require_POST
@requires_csrf_token
@info_wraper
def register(request):
    """
    """
    return profile_views.register(request)

@require_POST
@json_view
def nickname_check(request):
    """
    """
    return profile_views.nickname_check(request)

@require_POST
@json_view
@ajax_login_required
def logout(request):
    """
    User logout
    @param request:
    @return:
    """
    # return user_views.logout(request)
    pass

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
    # return user_views.update_user_info(request)
    pass

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
