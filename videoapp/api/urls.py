from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^video/$',views.VideoDetailAPIView.as_view(),name='Video'),
    url(r'^topic_wise_video/$',views.TopicWiseVideoDetailsAPIView.as_view(),name='topice_video'),
    url(r'^category_wise_video/$',views.CategoryWiseVideoDetailsAPIView.as_view(),name='category_video'),
    ]
