from django.conf import settings
from django.conf.urls import patterns, url, include
from flickr_stream.fps import views 

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^photos/$', views.PhotosView.as_view(), name='photos_html'),
    url(r'^photos\.json/$', views.PhotosJSON, name='photos_json'),
)


