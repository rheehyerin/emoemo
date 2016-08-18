from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from blog import views

app_name ="blog"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base/$', views.base, name="base"),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<post_pk>\d+)/comments/new/$', views.comment_new, name="comments"),
]