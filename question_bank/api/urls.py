from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^question/$',views.QuestionDetailAPIView.as_view(),name='QuestionDetail'),    
    #url(r'^question/$',views.QuestionDetailAPIView.as_view(),name='QuestionDetail'),
    url(r'^categoryWiseQuestion/$',views.categoryWiseQuestionDetailAPIView.as_view(),name='categoryWiseQuestion'),
    ]
