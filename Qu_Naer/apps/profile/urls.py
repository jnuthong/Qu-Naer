from django.conf.urls import patterns, url

import apps.profile.views

urlpatterns = patterns('',

    url(r'^get_user_info', apps.profile.views.get_user_info, name='get_user_info')
)