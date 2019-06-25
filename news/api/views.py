from rest_framework import generics
from django.utils import timezone
#:from celery.result import AsyncResult 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from news.models import *
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




class NewsDetailAPIView(APIView):
    #serializer_class = NewsSerializer
    def get(self, request, format=None):
        news_content =News.objects.all()   
        category_list=[]
        title_list=[]
        hindi_titles=[]
        hindi_new=[]
        content_list=[]
        date_list=[]
        source_list=[]
        link_list=[]
        for i in news_content:
            category=i.category
            title=i.title
            text= i.news_text
            dates=i.date
            sources=i.source
            links=i.link1
            hindi_ti=i.title_hindi
            hindi_content=i.hindi_news

            category_list.append(category)
            title_list.append(title)
            content_list.append(text)
            date_list.append(dates)
            source_list.append(sources)
            link_list.append(links)
            hindi_titles.append(hindi_ti)
            hindi_new.append(hindi_content)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(category_list,title_list,date_list,source_list,link_list,content_list,hindi_titles,hindi_new))
        final_news = []
        for a,b,c,d,e,f,g,h in contents:
            dict = {'category':a,'English_title':b,"Hindi_title":g,'date':c,'source':d,'link':e,'English_news':f,"Hindi_news":h}
            final_news.append(dict)
             #print(type(i))
             #context = {"date":date,"news_content":i}
         #print(len(dict))
        context={'news':final_news}
        return Response(context)


class DateWiseNewsDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        date = request.POST['date']
        print(date)
        dateWiseNews= News.objects.filter(date=date)
        #news_content = News.objects.all()
        #serialzer = NewsSerializer(dateWiseNews, many=True)
        #return Response(serialzer.data)
        category_list=[]
        title_list=[]
        content_list=[]
        date_list=[]
        source_list=[]
        link_list=[]
        hindi_titles = []
        hindi_new = []

        for i in dateWiseNews:
            category=i.category
            title=i.title
            text= i.news_text
            dates=i.date
            sources=i.source
            links=i.link1
            hindi_ti = i.title_hindi
            hindi_content = i.hindi_news

            category_list.append(category)
            title_list.append(title)
            content_list.append(text)
            date_list.append(dates)
            source_list.append(sources)
            link_list.append(links)
            hindi_titles.append(hindi_ti)
            hindi_new.append(hindi_content)

        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents = list(
            zip(category_list, title_list, date_list, source_list, link_list, content_list, hindi_titles, hindi_new))
        final_news = []
        for a, b, c, d, e, f, g, h in contents:
            dict = {'category': a, 'English_title': b, "Hindi_title": g, 'date': c, 'source': d, 'link': e,
                    'English_news': f, "Hindi_news": h}
            final_news.append(dict)
            # print(type(i))
            # context = {"date":date,"news_content":i}
        # print(len(dict))
        context = {'news': final_news}
        return Response(context)


class CatogoryWiseNewsDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        category_name = request.POST['category']
        CategoryWiseNews= News.objects.filter(category=category_name)
        category_list=[]
        title_list=[]
        content_list=[]
        date_list=[]
        source_list=[]
        link_list=[]
        hindi_titles = []
        hindi_new = []

        for i in CategoryWiseNews:
            category=i.category
            title=i.title
            text= i.news_text
            dates=i.date
            sources=i.source
            links=i.link1
            hindi_ti = i.title_hindi
            hindi_content = i.hindi_news


            category_list.append(category)
            title_list.append(title)
            content_list.append(text)
            date_list.append(dates)
            source_list.append(sources)
            link_list.append(links)
            hindi_titles.append(hindi_ti)
            hindi_new.append(hindi_content)


        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))

        contents = list(
            zip(category_list, title_list, date_list, source_list, link_list, content_list, hindi_titles, hindi_new))
        final_news = []
        for a, b, c, d, e, f, g, h in contents:
            dict = {'category': a, 'English_title': b, "Hindi_title": g, 'date': c, 'source': d, 'link': e,
                    'English_news': f, "Hindi_news": h}
            final_news.append(dict)
            # print(type(i))
            # context = {"date":date,"news_content":i}
        # print(len(dict))
        context = {'news': final_news}
        return Response(context)

    


