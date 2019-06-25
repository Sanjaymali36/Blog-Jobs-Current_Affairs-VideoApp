from rest_framework import generics
from django.utils import timezone
#:from celery.result import AsyncResult 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from jobs.models import *
from django.http import Http404, HttpResponse
from .serializers import *

import json
import random
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

import datetime
from decimal import Decimal


from django.contrib.auth.models import User


class VideoDetailAPIView(APIView):
    def get(self, request, format=None):
        video_content =Video.objects.all()
        #serialzer = VideoSerializer(video_content,many=True)
        #return Response(serialzer.data)
        print('hiii')
        publisher=[]
        content_list=[]
        category_list=[]
        title_list=[]
        topic_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]
        link3_list=[]

        for p in video_content:
            category=p.video_category
            topic=p.video_topic
            title=p.video_title
            upload_date=p.upload_date
            text=p.content
            link1=p.link1
            link2=p.link2
            link3=p.link3
            pub=p.publisher
            content_list.append(text)
            category_list.append(category)
            title_list.append(title)
            topic_list.append(topic)
            date_list.append(upload_date)
            link1_list.append(link1)
            link2_list.append(link2)
            link3_list.append(link3)
            publisher.append(pub)
            #print('api working')
        video_content=zip(category_list,topic_list,title_list,date_list,link1_list,link2_list,link3_list,content_list,publisher)
        video_list=[]
        for a,b,c,d,e,f,g,h,i in video_content:
            dict = {'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f,'link3':g,'content':h,'publisher':i}
            video_list.append(dict)
        context={'video_content':video_list}
        return Response(context)


"""

class CategoryWiseVideoDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        video_category = request.POST['video_category']
        print(video_category)
        categoryWisevideo= Video.objects.filter(video_category=video_category)
        serialzer = VideoSerializer(categoryWisevideo,many=True)
        return Response(serialzer.data)

"""

class CategoryWiseVideoDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        video_category = request.POST['video_category']
        print(video_category)
        categoryWisevideo= Video.objects.filter(video_category=category)
        print('hiii')
        publisher=[]
        content_list=[]
        category_list=[]
        title_list=[]
        topic_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]
        link3_list=[]

        for p in categoryWisevideo:
            category=p.video_category
            topic=p.video_topic
            title=p.video_title
            upload_date=p.upload_date
            text=p.content
            link1=p.link1
            link2=p.link2
            link3=p.link3
            pub=p.publisher
            content_list.append(text)
            category_list.append(category)
            title_list.append(title)
            topic_list.append(topic)
            date_list.append(upload_date)
            link1_list.append(link1)
            link2_list.append(link2)
            link3_list.append(link3)
            publisher.append(pub)
            #print('api working')
        video_content=zip(category_list,topic_list,title_list,date_list,link1_list,link2_list,link3_list,content_list)
        video_list=[]
        for a,b,c,d,e,f,g,h in video_content:
            dict = {'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f,'link3':g,'content':h}
            video_list.append(dict)
        context={'video_content':video_list}
        return Response(context)










"""
class TopicWiseVideoDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        video_topic = request.POST['video_topic']
        print(video_topic)
        topicWiseVideo= Video.objects.filter(video_topic=video_topic)
        serialzer = VideoSerializer(topicWiseVideo,many=True)
        return Response(serialzer.data)
"""





class TopicWiseVideoDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        video_topic = request.POST['topic']
        print(video_topic)
        topicWiseVideo= Video.objects.filter(video_topic=video_topic)

        print('hiii')
        publisher=[]
        content_list=[]
        category_list=[]
        title_list=[]
        topic_list=[]
        date_list=[]
        link1_list=[]
        link2_list=[]
        link3_list=[]

        for p in topicWiseVideo:
            category=p.video_category
            topic=p.video_topic
            title=p.video_title
            upload_date=p.upload_date
            text=p.content
            link1=p.link1
            link2=p.link2
            link3=p.link3
            pub=p.publisher
            content_list.append(text)
            category_list.append(category)
            title_list.append(title)
            topic_list.append(topic)
            date_list.append(upload_date)
            link1_list.append(link1)
            link2_list.append(link2)
            link3_list.append(link3)
            publisher.append(pub)
            #print('api working')
        video_content=zip(category_list,topic_list,title_list,date_list,link1_list,link2_list,link3_list,content_list)
        video_list=[]
        for a,b,c,d,e,f,g,h in video_content:
            dict = {'category':a,'topic':b,'title':c,'date':d,'link1':e,'link2':f,'link3':g,'content':h}
            video_list.append(dict)
        context={'video_content':video_list}
        return Response(context)

