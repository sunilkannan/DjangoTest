from django.conf.urls import patterns, include, url
from django.contrib import admin
from EXAPP.views import *
from MONGOAPP.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile', FeedCreate.as_view(), name = 'profile'),
    url(r'^$', DisplayHome.as_view(), name = 'Home'),
    url(r'^login/',LoginPage.as_view(),name = 'Login'),
    #url(r'^chess/$', chessplace.ChessView.as_view(template_name='chess.html'), name='chess'),
    # MONGOAPP urls
    url(r'^MONGOAPP', MongoLogin.as_view(),name = 'Mongo App login')
    


)

