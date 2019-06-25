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


class JobsDetailAPIView(APIView):
    #serializer_class = NewsSerializer
    def get(self, request, format=None):
        jobs_content =Jobs.objects.all()

        title_list=[]
        department_list=[]
        loction_list=[]
        notification_list=[]
        qualifiction_list=[]
        admit_card_list=[]
        result_list=[]
        apply_list=[]
        more_detail_list=[]
        date_list=[]
        link3_list=[]
        syllabus_list=[]
        jobs_info_list=[]
        for i in jobs_content:
            title=i.job_title
            department=i.job_department
            loction=i.job_location
            notifiction=i.notification
            qualification=i.qualification
            dates=i.last_date
            admitCard=i.admit_card
            results=i.result
            applyLink=i.apply_link
            more_details=i.more_detail
            links=i.link3
            syllb=i.syllabus
            job_info=i.jobs_info

            title_list.append(title)
            department_list.append(department)
            loction_list.append(loction)
            notification_list.append(notifiction)
            qualifiction_list.append(qualification)
            admit_card_list.append(admitCard)
            result_list.append(results)
            apply_list.append(applyLink)
            more_detail_list.append(more_details)
            date_list.append(dates)
            link3_list.append(links)
            syllabus_list.append(syllb)
            jobs_info_list.append(job_info)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(title_list,department_list,loction_list,notification_list,qualifiction_list,admit_card_list,result_list,apply_list,more_detail_list,date_list,link3_list,syllabus_list,jobs_info_list))
        final_news = []
        for a,b,c,d,e,f,g,h,i,j,k,l,m in contents:
            dict = {'job_title':a,'job_department':b,'job_location':c,'notification':d,'qualification':e,'admit_card':f,'result':g,'apply_link':h,'date':i,'more_detail':j,'link':k,'syllabus':l,'jobs_info':m}
            final_news.append(dict)
             #print(type(i))
             #context = {"date":date,"news_content":i}
         #print(len(dict))
        context={'jobs':final_news}
        return Response(context)


class DepartmentWiseJobDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        department = request.POST['department']
        print(department)
        departmentWiseJobs= Jobs.objects.filter(job_department=department)

        title_list=[]
        department_list=[]
        loction_list=[]
        notification_list=[]
        qualifiction_list=[]
        admit_card_list=[]
        result_list=[]
        apply_list=[]
        more_detail_list=[]
        date_list=[]
        link3_list=[]
        syllabus_list=[]
        jobs_info_list=[]
        for i in departmentWiseJobs:
            title=i.job_title
            department=i.job_department
            loction=i.job_location
            notifiction=i.notification
            qualification=i.qualification
            dates=i.last_date
            admitCard=i.admit_card
            results=i.result
            applyLink=i.apply_link
            more_details=i.more_detail
            links=i.link3
            syllb=i.syllabus
            job_info=i.jobs_info

            title_list.append(title)
            department_list.append(department)
            loction_list.append(loction)
            notification_list.append(notifiction)
            qualifiction_list.append(qualification)
            admit_card_list.append(admitCard)
            result_list.append(results)
            apply_list.append(applyLink)
            more_detail_list.append(more_details)
            date_list.append(dates)
            link3_list.append(links)
            syllabus_list.append(syllb)
            jobs_info_list.append(job_info)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(title_list,department_list,loction_list,notification_list,qualifiction_list,admit_card_list,result_list,apply_list,date_list,more_detail_list,link3_list,syllabus_list,jobs_info_list))
        final_news = []
        for a,b,c,d,e,f,g,h,i,j,k,l,m in contents:
            dict = {'job_title':a,'job_department':b,'job_location':c,'notification':d,'qualification':e,'admit_card':f,'result':g,'apply_link':h,'date':i,'more_detail':j,'link':k,'syllabus':l,'jobs_info':m}
            final_news.append(dict)
             #print(type(i))
             #context = {"date":date,"news_content":i}
         #print(len(dict))
        context={'jobs':final_news}
        return Response(context)






class LoctionWiseJobDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        loction = request.POST['location']
        print(loction)
        loctionWiseJobs= Jobs.objects.filter(job_location=loction)
        title_list=[]
        department_list=[]
        loction_list=[]
        notification_list=[]
        qualifiction_list=[]
        admit_card_list=[]
        result_list=[]
        apply_list=[]
        more_detail_list=[]
        date_list=[]
        link3_list=[]
        syllabus_list=[]
        jobs_info_list=[]
        for i in loctionWiseJobs:
            title=i.job_title
            department=i.job_department
            loction=i.job_location
            notifiction=i.notification
            qualification=i.qualification
            dates=i.last_date
            admitCard=i.admit_card
            results=i.result
            applyLink=i.apply_link
            more_details=i.more_detail
            links=i.link3
            syllb=i.syllabus
            job_info=i.jobs_info

            title_list.append(title)
            department_list.append(department)
            loction_list.append(loction)
            notification_list.append(notifiction)
            qualifiction_list.append(qualification)
            admit_card_list.append(admitCard)
            result_list.append(results)
            apply_list.append(applyLink)
            more_detail_list.append(more_details)
            date_list.append(dates)
            link3_list.append(links)
            syllabus_list.append(syllb)
            jobs_info_list.append(job_info)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(title_list,department_list,loction_list,notification_list,qualifiction_list,admit_card_list,result_list,apply_list,date_list,more_detail_list,link3_list,syllabus_list,jobs_info_list))
        final_news = []
        for a,b,c,d,e,f,g,h,i,j,k,l,m in contents:
            dict = {'job_title':a,'job_department':b,'job_location':c,'notification':d,'qualification':e,'admit_card':f,'result':g,'apply_link':h,'date':i,'more_detail':j,'link':k,'syllabus':l,'jobs_info':m}
            final_news.append(dict)
             #print(type(i))
             #context = {"date":date,"news_content":i}
         #print(len(dict))
        context={'jobs':final_news}
        return Response(context)



class QualificationWiseJobDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        qualification = request.POST['qualification']
        print(qualification)
        qualificationWiseJobs= Jobs.objects.filter(qualification=qualification)
        title_list=[]
        department_list=[]
        loction_list=[]
        notification_list=[]
        qualifiction_list=[]
        admit_card_list=[]
        result_list=[]
        apply_list=[]
        more_detail_list=[]
        date_list=[]
        link3_list=[]
        syllabus_list=[]
        jobs_info_list=[]
        for i in qualificationWiseJobs:
            title=i.job_title
            department=i.job_department
            loction=i.job_location
            notifiction=i.notification
            qualification=i.qualification
            dates=i.last_date
            admitCard=i.admit_card
            results=i.result
            applyLink=i.apply_link
            more_details=i.more_detail
            links=i.link3
            syllb=i.syllabus
            job_info=i.jobs_info

            title_list.append(title)
            department_list.append(department)
            loction_list.append(loction)
            notification_list.append(notifiction)
            qualifiction_list.append(qualification)
            admit_card_list.append(admitCard)
            result_list.append(results)
            apply_list.append(applyLink)
            more_detail_list.append(more_details)
            date_list.append(dates)
            link3_list.append(links)
            syllabus_list.append(syllb)
            jobs_info_list.append(job_info)
        # #print('post api working')
        # print(len(title_list))
        # print(len(content_list))
        contents=list(zip(title_list,department_list,loction_list,notification_list,qualifiction_list,admit_card_list,result_list,apply_list,date_list,more_detail_list,link3_list,syllabus_list,jobs_info_list))
        final_news = []
        for a,b,c,d,e,f,g,h,i,j,k,l,m in contents:
            dict = {'job_title':a,'job_department':b,'job_location':c,'notification':d,'qualification':e,'admit_card':f,'result':g,'apply_link':h,'date':i,'more_detail':j,'link':k,'syllabus':l,'jobs_info':m}
            final_news.append(dict)
        context={'jobs':final_news}
        return Response(context)








""" 
class LoctionWiseJobDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        loction = request.POST['loction']
        print(loction)
        loctionWiseJobs= Jobs.objects.filter(job_location=loction)
        serialzer = JobsSerializer(loctionWiseJobs,many=True)
        return Response(serialzer.data)

class QualificationWiseJobDetailsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        qualification = request.POST['qualification']
        print(qualification)
        qualificationWiseJobs= Jobs.objects.filter(qualification=qualification)
        serialzer = JobsSerializer(qualificationWiseJobs,many=True)
        return Response(serialzer.data)
"""
