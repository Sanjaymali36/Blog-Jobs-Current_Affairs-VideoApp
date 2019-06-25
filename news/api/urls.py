from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^news/$',views.NewsDetailAPIView.as_view(),name='NewsDetail'),
    url(r'^datewiseNews/$',views.DateWiseNewsDetailsAPIView.as_view(),name='date'),
    url(r'^categoryNews/$',views.CatogoryWiseNewsDetailsAPIView.as_view(),name='Newscategory'),
    ]
