from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_id>\d+)/comment/new/$', views.comment_create, name='comment_create'),
    url(r'^(?P<post_id>\d+)/comment/new/(?P<comment_id>\d+)/edit/$', views.comment_update, name='comment_update'),
    url(r'^(?P<post_id>\d+)/comment/new/(?P<comment_id>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]