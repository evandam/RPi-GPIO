from django.conf.urls import patterns, url

from gpio import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<switch_id>\d+)/(?P<state>0|1)/$', views.control_switch, name='switch')
)
