from rest_framework import generics
from django.utils import timezone
#:from celery.result import AsyncResult 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from blog.models import *
from django.http import Http404, HttpResponse
from .serializers import *
from blog.api.views import *
import json
import random
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

import datetime
from decimal import Decimal
#from exponent_server_sdk import DeviceNotRegisteredError
#from exponent_server_sdk import PushClient
#from exponent_server_sdk import PushMessage
#from exponent_server_sdk import PushResponseError
#from exponent_server_sdk import PushServerError
#from requests.exceptions import ConnectionError
#from requests.exceptions import HTTPError

from django.views.generic.list import ListView



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import helpers


class LatestBlogAPIView(APIView):
    # serializer_class = LatestSerializer
    def get(self, request, format=None):
        all_blogs = latest.objects.all()[1:]

        user_list = []
        category_list = []
        topic_list = []
        title_list = []
        content_list = []
        date_list = []
        link1_list = []
        link2_list = []

        for i in all_blogs:
            creater = i.creater.username
            categories = i.category
            topics = i.topic
            titles = i.title
            texts = i.content
            dates = i.creation_date
            links = i.link1
            links2 = i.link2

            user_list.append(creater)
            category_list.append(categories)
            title_list.append(titles)
            topic_list.append(topics)
            content_list.append(texts)
            date_list.append(dates)
            link1_list.append(links)
            link2_list.append(links2)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents = list(
            zip(user_list, category_list, topic_list, title_list, date_list, link1_list, link2_list, content_list))
        final_blog = []
        for z, a, b, c, d, e, f, g in contents:
            dict = {'creater': z, 'category': a, 'topic': b, 'title': c, 'date': d, 'link1': e, 'link2': f,
                    'blog_content': g}
            final_blog.append(dict)
        print(final_blog)
        context = {'blogs': final_blog}
        return Response(context)


class blog_pageAPIView(APIView):
    def post(self,request,*args,**kwargs):
        #page = request.GET.get('page')
        page = request.POST['page']

        print(page)
        blog = Paginator(latest.objects.order_by("-id").all().reverse(),4)
        try:
        # create Page object for the given page
            post = blog.page(page)
        except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
            post = blog.page(1)
        except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
            post = blog.page(blog.num_pages)

        #blog = Paginator(latest.objects.order_by("-id").all().reverse(),5)
        #posts = helpers.pg_records(request, posts, 2)
        #post=blog.page(page)
        #return render(request, 'blog/post_list.html', {'posts': posts})
        serialzer = LatestSerializer(post, many=True)
        return Response(serialzer.data)



class firstBlogAPIView(APIView):
 
    def post(self,request,*args,**kwargs):
        #page = request.GET.get('page')
        page = request.POST['page']

        posts = Paginator(latest.objects.order_by("-id").all().reverse(),5)
        try:
            postss=posts.page(page)
        except PageNotAnInteger:
            postss=posts.page(1)
        except EmptyPage:
            postss=posts.page(posts.num_pages)

        slug_list=[]
        all_id=[]
        user_list=[]
        category_list=[]
        topic_list=[]
        title_list=[]
        content_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]

        for i in postss:
            slug=i.slug
            ids=i.id
            creater=i.creater.username
            categories=i.category
            topics=i.topic
            titles=i.title
            texts= i.content
            dates=i.creation_date
            links=i.link1
            links2=i.link2
            
            slug_list.append(slug)
            all_id.append(ids)
            user_list.append(creater)
            category_list.append(categories)
            title_list.append(titles)
            topic_list.append(topics)
            content_list.append(texts)
            date_list.append(dates)
            link1_list.append(links)
            link2_list.append(links2)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(slug_list,all_id,user_list,category_list,topic_list,title_list,date_list,link1_list,link2_list))
        final_blog = []
        for x,y,z,a,b,c,d,e,f in contents:
            dict = {'slug':x,'blog_id':y,'creater':z,'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f}
            final_blog.append(dict)
        print(final_blog)
        context={'blogs':final_blog}
        return Response(context)

class IdWiseBlogAPIView(APIView):
    def post(self,request,*args,**kwargs):
        ids = request.POST['id']
        IdWiseBlog= latest.objects.filter(id=ids)
        slug_list=[]
        category_list=[]
        topic_list=[]
        title_list=[]
        content_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]

        for i in IdWiseBlog:
            slug=i.slug
            categories=i.category
            topics=i.topic
            titles=i.title
            texts= i.content
            dates=i.creation_date
            links=i.link1
            links2=i.link2

            slug_list.append(slug)
            category_list.append(categories)
            title_list.append(titles)
            topic_list.append(topics)
            content_list.append(texts)
            date_list.append(dates)
            link1_list.append(links)
            link2_list.append(links2)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(slug_list,category_list,topic_list,title_list,date_list,link1_list,link2_list,content_list))
        final_blog = []
        for z,a,b,c,d,e,f,g in contents:
            dict = {'slug':z,'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f,'blog_content':g}
            final_blog.append(dict)
        print(final_blog)
        context={'blogs':final_blog}
        return Response(context)









class CatogoryWiseBlogAPIView(APIView):
    def post(self,request,*args,**kwargs):
        category_name = request.POST['category']
        CategoryWiseBlog= latest.objects.filter(category=category_name)

        user_list=[]
        category_list=[]
        topic_list=[]
        title_list=[]
        content_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]

        for i in CategoryWiseBlog:
            creater=i.creater.username
            categories=i.category
            topics=i.topic
            titles=i.title
            texts= i.content
            dates=i.creation_date
            links=i.link1
            links2=i.link2

            user_list.append(creater)
            category_list.append(categories)
            title_list.append(titles)
            topic_list.append(topics)
            content_list.append(texts)
            date_list.append(dates)
            link1_list.append(links)
            link2_list.append(links2)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(user_list,category_list,topic_list,title_list,date_list,link1_list,link2_list,content_list))
        final_blog = []
        for z, a,b,c,d,e,f,g in contents:
            dict = {'creater':z,'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f,'blog_content':g}
            final_blog.append(dict)
        #print(final_blog)
        #p=paginator(final_blog)
        context={'blogs':final_blog}
        return Response(context)

class TopicWiseBlogAPIView(APIView):
    def post(self,request,*args,**kwargs):
        topic = request.POST['topic']
        TopicWiseBlog= latest.objects.filter(topic=topic)
        category_list=[]
        topic_list=[]
        title_list=[]
        content_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]

        for i in TopicWiseBlog:
            categories=i.category
            topics=i.topic
            titles=i.title
            texts= i.content
            dates=i.creation_date
            links=i.link1
            links2=i.link2
            category_list.append(categories)
            title_list.append(titles)
            topic_list.append(topics)
            content_list.append(texts)
            date_list.append(dates)
            link1_list.append(links)
            link2_list.append(links2)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(category_list,topic_list,title_list,date_list,link1_list,link2_list,content_list))
        final_blog = []
        for a,b,c,d,e,f,g in contents:
            dict = {'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f,'blog_content':g}
            final_blog.append(dict)
        print(final_blog)
        context={'blogs':final_blog}
        return Response(context)













"""
class firstBlogAPIView(APIView):
    #serializer_class = LatestSerializer
    def get(self, request, format=None):
        all_blogs = latest.objects.all().order_by('id').reverse()

        slug_list=[]
        all_id=[]
        user_list=[]
        category_list=[]
        topic_list=[]
        title_list=[]
        content_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]

        for i in all_blogs:
            slug=i.slug
            ids=i.id
            creater=i.creater.username
            categories=i.category
            topics=i.topic
            titles=i.title
            texts= i.content
            dates=i.creation_date
            links=i.link1
            links2=i.link2
            
            slug_list.append(slug)
            all_id.append(ids)
            user_list.append(creater)
            category_list.append(categories)
            title_list.append(titles)
            topic_list.append(topics)
            content_list.append(texts)
            date_list.append(dates)
            link1_list.append(links)
            link2_list.append(links2)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(slug_list,all_id,user_list,category_list,topic_list,title_list,date_list,link1_list,link2_list))
        final_blog = []
        for x,y,z,a,b,c,d,e,f in contents:
            dict = {'slug':x,'blog_id':y,'creater':z,'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f}
            final_blog.append(dict)
        print(final_blog)
        context={'blogs':final_blog}
        return Response(context)
"""







class BlogListView(ListView):
    def get(self, request, *args, **kwargs):
        blogs = latest.objects.all()

        serialzer = LatestSerializer(blogs, many=True)
        return Response(serialzer.data)




class BlogDetailAPIView(APIView):
    #serializer_class = BlogDisplaySerializer
    def get(self, request, format=None):
        all_blogs = Blog.objects.all()
        serializer = BlogSerializer(all_blogs, many=True)
        return Response(serializer.content)








"""s
class LatestBlogAPIView(APIView):
    #serializer_class = LatestSerializer
    def get(self, request, format=None):
        all_blogs = latest.objects.all()
        serialzer = LatestSerializer(all_blogs, many=True)
        return Response(serialzer.data)

"""




"""
class CatogoryWiseBlogAPIView(APIView):
    def post(self,request,*args,**kwargs):
        category_name = request.POST['category']
        CatogoryWiseBlog= latest.objects.filter(category=category_name)
        serialzer = LatestSerializer(CatogoryWiseBlog, many=True)
        return Response(serialzer.data)
   """


"""
class BlogDetailAPIView(APIView):
    #serializer_class = BlogDisplaySerializer
    def get(self, request, format=None):
        all_blogs = Blog.objects.all()
        serialzer = BlogSerializer(all_blogs, many=True)
        return Response(serialzer.data)
        
        topics=Topic.objects.all()
        Title_list=[]
        Topics_list=[]
        Blogs=[]
        for post in all_blogs:
            text=post.Blog_Text
            titles=post.title
            Blogs.append(text)
            Title_list.append(titles)
            time=post.updated_at
        for topic in topics:
            topic_name=topic.subject
            Topics_list.append(topic_name)
        context = {'Topics_list':Topics_list, 'Titles':Title_list,'updated_at':time,'Blogs':Blogs}
        return Response(context)
    
"""
