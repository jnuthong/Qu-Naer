__author__ = 'J Hong'
from django.contrib import admin
from django.conf.urls import patterns, url
from mapi import views

admin.autodiscover()

urlpatterns = patterns('',
    # User
    url(r'^login', views.login, name='user login'),
    url(r'^logout', views.logout, name='user logout'),
    url(r'^get_user_info', views.get_user_info, name='get user info'),
    url(r'^update_user_info', views.update_user_info, name='update user info'),
    url(r'^register', views.register, name='register user'),

    # Third user
    url(r'^check_third_user_is_exist', views.check_third_user_is_exist, name='check_third_user_is_exist'),
    url(r'^update_third_user_info', views.update_third_user_info, name='update third user info'),
    url(r'^third_user_login', views.third_user_login, name='third_user_login'),

    # CSRF test
    url(r'get_test', views.get_test_csrf, name="this is test for get crsf token"),
)