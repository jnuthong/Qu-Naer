__author__ = 'J Hong'
from django.contrib import admin
from django.conf.urls import patterns, url
from mapi import views

admin.autodiscover()

urlpatterns = patterns('',
    # User
    url(r'^logout', views.logout, name='user logout'),
    url(r'^get_user_info', views.get_user_info, name='get user info'),
    url(r'^update_user_info', views.update_user_info, name='update user info'),
    url(r'^register', views.register, name='register user'),
    url(r'nickname_check', views.nickname_check, name='check the unique of user nick'),

    # Third user
    url(r'^check_third_user_is_exist', views.check_third_user_is_exist, name='check_third_user_is_exist'),
    url(r'^update_third_user_info', views.update_third_user_info, name='update third user info'),
    url(r'^third_user_login', views.third_user_login, name='third_user_login'),
)