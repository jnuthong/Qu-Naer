from django.conf.urls import patterns, include, url
from django.contrib import admin
import mapi.urls
import j_blog.urls
import main.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Qu_Naer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # personal blog url patcher
    url(r'^j_blog/', include(j_blog.urls)),

    # url(r'^$', include(mapi.urls), name='home'),

    url(r'^signup/', main.views.views_signup),
    url(r'^validEmail/', main.views.views_validEmail),
    url(r'^activeAccount', main.views.activeAccount),
    url(r'^signin', main.views.views_signin),

    url(r'^home/', include(mapi.urls)),
    url(r'^mapi/', include(mapi.urls)),
    url(r'test/', main.views.views_test),
)
