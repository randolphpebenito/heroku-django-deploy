from django.conf.urls import include, url
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^shorten/(?P<pk>[0-9]+)/$', views.show_url_shorten, name='url_shorten'),
    url(r'^(?P<urlshort>[a-zA-Z0-9]{7})/$', views.redirect_url_shorten, name='url_shorten_redirect'),

    url(r'^admin/', include(admin.site.urls)),
]

