from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'accounts/login.html',
        }),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^index/$', views.index, name="index"),
    url(r'^follow/$', views.follow, name="follow"),
    url(r'^request_list/$', views.request_list, name="request_list"),
    url(r'^friend_list/$', views.friend_list, name="friend_list"),
    url(r'^request_list/(?P<pk>\d+)/del/$', views.del_request_list, name="del_request_list"),
    url(r'^request_list/(?P<pk>\d+)/apv/$', views.aprv_request_list, name="aprv_request_list"),
    url(r'^follow/search/$', views.search_follow, name="search_follow"),
]