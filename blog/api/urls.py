from django.conf.urls import url
from blog.api import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^latestblog/$',views.LatestBlogAPIView.as_view(),name='LatestBlog'), # ALL blogs get request
    url(r'^blogs/$',views.blog_pageAPIView.as_view(),name='post_list'), # for blog by page number
    url(r'^category_wise_blog/$',views.CatogoryWiseBlogAPIView.as_view(),name='Category_Blog'),
    url(r'^id_wise_blog/$',views.IdWiseBlogAPIView.as_view(),name='id_Blog'),
    url(r'^topic_wise_blog/$',views.TopicWiseBlogAPIView.as_view(),name='Topic_Blog'),
    #url(r'^$',views.BlogDetailAPIView.as_view(),name='BlogDetail'),
    #url(r'^firstblog$',views.firstBlogAPIView.as_view(),name='firstBlog'),

    url(r'^blog_list/$',views.BlogListView.as_view(),name='blog_list'),

    ]
