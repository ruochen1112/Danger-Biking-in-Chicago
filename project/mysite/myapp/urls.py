from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^home/$', views.home, name = 'home'),
    url(r'^map/$', views.map, name = 'map'),
    url(r'^presentation/$', views.presentation, name = 'presentation'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^csv/$', views.csv),
    url(r'^csv/(?P<station>[0-9]+)/$', views.csv),
    url(r'^pic/(?P<station>[0-9]+)/$', views.pic, name='pic'),
    url(r'^plot/$', views.plot, name='plot'),
]
