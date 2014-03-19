from django.conf.urls import patterns, url

import apps.oauth.views

urlpatterns = patterns('',

    url(r'^check_third_user_is_exist', apps.oauth.views.check_third_user_is_exist, name='check_third_user_is_exist'),
    url(r'^update_third_user_info', apps.oauth.views.update_third_user_info, name='update_third_user_info'),
    url(r'^third_user_login', apps.oauth.views.third_user_login, name='third_user_login')
)