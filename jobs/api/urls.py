from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jobs/$',views.JobsDetailAPIView.as_view(),name='JobsDetail'),
    url(r'^departmentwisejobs/$',views.DepartmentWiseJobDetailsAPIView.as_view(),name='departmentWiseJobs'),
    url(r'^qualificationWiseJobs/$',views.QualificationWiseJobDetailsAPIView.as_view(),name='QualificationWiseJobs'),
    url(r'^loctionWiseJobs/$',views.LoctionWiseJobDetailsAPIView.as_view(),name='LoctionWiseJobs')

    ]
