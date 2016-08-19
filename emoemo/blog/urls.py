from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from blog import views

app_name ="blog"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_id>\d+)/edit/$', views.post_update, name='post_update'),
    url(r'^(?P<post_id>\d+)/delete$', views.post_delete, name='post_delete'),
    url(r'^(?P<post_id>\d+)/comment/new/$', views.comment_create, name='comment_create'),
    url(r'^(?P<post_id>\d+)/(?P<comment_id>\d+)/edit/$', views.comment_update, name='comment_update'),
    url(r'^(?P<post_id>\d+)/(?P<comment_id>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]