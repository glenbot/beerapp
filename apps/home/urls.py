from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('home',                  
    url(r'^$', 'views.index', name="home"),
)