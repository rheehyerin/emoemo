from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views

app_name="accounts"
urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'blog/index.html',
        }),
    url(r'^login/$', views.my_log, name='my_log'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', logout, name='logout', kwargs={
        'template_name' : 'blog/index.html',
        }),
    url(r'^index/$', views.index, name="index"),
    url(r'^follow/$', views.follow),
    url(r'^request_list/$', views.request_list, name="request_list"),
    url(r'^friend_list/$', views.friend_list, name="friend_list"),
    url(r'^request_list/(?P<pk>\d+)/del/$', views.del_request_list, name="del_request_list"),
    url(r'^request_list/(?P<pk>\d+)/apv/$', views.aprv_request_list, name="aprv_request_list"),
]