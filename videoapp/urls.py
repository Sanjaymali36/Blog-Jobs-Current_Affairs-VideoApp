from django.conf.urls import url
from videoapp import views
app_name = 'videoapp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>[-\w]+)/$', views.entry, name='entry'),
    url(r'^categories/(?P<pk>\d+)/$', views.category_topics, name='category_topics'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),

    #url(r'^title/(?P<pk>\d+)/$', views.get_title, name='get_title'),


]
