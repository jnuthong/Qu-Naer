from django.conf.urls import patterns, include, url
from j_blog import views

urlpatterns = patterns('',
                       url(r'^test/', views.test),
                       url(r'^get_time_index/', views.get_time_index_v),
                       url(r'^get_posts_by_time_index/', views.get_post_by_time_index_v),
                       url(r'^get_posts_by_topic/', views.get_post_by_topic_v),
                       )