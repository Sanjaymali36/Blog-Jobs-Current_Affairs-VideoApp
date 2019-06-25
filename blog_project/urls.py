"""bodhiai_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url,include
from blog_project import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='homepage' ),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^videoapp/', include('videoapp.urls', namespace='videoapp')),
    url(r'^gkapp/', include('gk_app.urls', namespace='gk_app')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^jobs/', include('jobs.urls',namespace='jobs')),
    url(r'^question/', include('question_bank.urls',namespace='question_bank')),

    url(r'^api/', include('news.api.urls')),
    url(r'^api/blog/', include('blog.api.urls')),
    url(r'^api/jobs/', include('jobs.api.urls')),
    url(r'^api/video/', include('videoapp.api.urls')),

    url(r'^api/question/', include('question_bank.api.urls'))
]
