from rest_framework import generics
from django.utils import timezone
#:from celery.result import AsyncResult
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from question_bank.models import *
from django.http import Http404, HttpResponse
from .serializers import *
from random import *
import json
import random
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)

import datetime
from decimal import Decimal

class QuestionDetailAPIView(APIView):

    def get(self, request, format=None):
        question_content =SSCquestions.objects.all()
        ids=[]
        category_list = []
        language_list = []
        content_list = []
        date_list = []
        source_list = []
        picture_list = []
        choice_list=[]
        for i in question_content:
            ques_id=i.id
            category = i.section_category
            text = i.text[4:]
            language = i.language
            sources = i.source
            picture = i.picture
            dates = i.dateInserted

            choices=i.choices_set.all()    #for choices

            choice_id=[]
            predicament_list = []
            text_list = []
            choice_pic_list = []
            explanation_list = []
            explanationPicture_list = []
            final_choices_list=[]
            for j in choices:
                ch_id=j.id
                predicament = j.predicament
                texts = j.text
                pictures = j.picture
                explanation = j.explanation
                explanationPicture = j.explanationPicture

                choice_id.append(ch_id)
                predicament_list.append(predicament)
                text_list.append(texts)
                choice_pic_list.append(pictures)
                explanation_list.append(explanation)
                explanationPicture_list.append(explanationPicture)

                choices_content = list(zip(choice_id, predicament_list, text_list, choice_pic_list, explanation_list,
                                           explanationPicture_list))
                final_choices = []
                for z, a, b, c, d, e, in choices_content:
                    choice_dict = {'id': z, 'predicament': a, 'text': b, 'picture': c, 'explanation': d,
                                   'explanationPicture': e}
                    final_choices.append(choice_dict)
                final_choices_list.append(final_choices)
            

            ids.append(ques_id)
            choice_list.append(final_choices)
            #print(choice_list)
            category_list.append(category)
            content_list.append(text)
            language_list.append(language)
            source_list.append(sources)
            picture_list.append(picture)
            date_list.append(dates)

        contents = list(zip(ids, category_list, content_list, language_list, source_list, picture_list, date_list, choice_list))
        final_ques = []
        
        for z, a, b, c, d, e, f, g in contents:
            dict = {'id': z, 'section_category': a, 'text': b, 'language': c, 'source': d, 'picture': e,
                    'dateInserted': f, 'choices': g}
            final_ques.append(dict)

        new_latest = []
        for fq in range(10):
            if len(new_latest) ==5:
                break
            random_qu = random.choice(final_ques)
            rq_id = random_qu['id']
            try:
                prev_ques = visitedQuestion.objects.get(qid=rq_id)
                print("in try")
                continue
            except Exception as e:
                print(str(e))
                prev_ques = visitedQuestion()
                prev_ques.qid = random_qu['id']
                prev_ques.save()
                new_latest.append(random_qu)
                print("in except")

        context = {'Questions': new_latest}
        return Response(context)
        #previous_question=vistedQuestion.objects.all()    
        #if len(final_ques) >0:


        #    latest = random.sample(final_ques,20)  
        
        #    context = {'Questions':latest}
        #    return Response(context)
        #else:
        #    context = {'Questions':"NO question for U"}
        #    return Response(context)

class categoryWiseQuestionDetailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print('hello')
        data = request.data
        #category = request.POST['section_category']
        category = data['section_category']
        print(category)
        question_content = SSCquestions.objects.filter(section_category=category)
        ids=[]
        category_list = []
        language_list = []
        content_list = []
        date_list = []
        source_list = []
        picture_list = []
        choice_list=[]
        for i in question_content:
            ques_id=i.id
            category = i.section_category

            text = i.text[4:]

            language = i.language
            sources = i.source
            picture = i.picture
            dates = i.dateInserted

            choices=i.choices_set.all()    #for choices

            choice_id=[]
            predicament_list = []
            text_list = []
            choice_pic_list = []
            explanation_list = []
            explanationPicture_list = []
            final_choices_list=[]
            for j in choices:
                ch_id=j.id
                predicament = j.predicament
                texts = j.text
                pictures = j.picture
                explanation = j.explanation
                explanationPicture = j.explanationPicture

                choice_id.append(ch_id)
                predicament_list.append(predicament)
                text_list.append(texts)
                choice_pic_list.append(pictures)
                explanation_list.append(explanation)
                explanationPicture_list.append(explanationPicture)

                choices_content = list(zip(choice_id,predicament_list, text_list, choice_pic_list, explanation_list, explanationPicture_list))
                final_choices = []
                for z, a, b, c, d, e, in choices_content:
                    choice_dict = {'id': z, 'predicament': a, 'text': b, 'picture': c, 'explanation': d,
                                   'explanationPicture': e}
                    final_choices.append(choice_dict)
                    # print(final_choices)
                final_choices_list.append(final_choices)

            ids.append(ques_id)
            choice_list.append(final_choices)
            category_list.append(category)
            content_list.append(text)
            language_list.append(language)
            source_list.append(sources)
            picture_list.append(picture)
            date_list.append(dates)

        contents = list(
            zip(ids,category_list, content_list, language_list, source_list, picture_list, date_list, choice_list))
        final_ques = []
        for z, a, b, c, d, e, f, g in contents:
            dict = {'id': z, 'section_category': a, 'text': b, 'language': c, 'source': d, 'picture': e,
                    'dateInserted': f, 'choices': g}
            final_ques.append(dict)
        new_latest = []
        for fq in range(10):
            if len(new_latest) ==5:
                break
            random_qu = random.choice(final_ques)
            rq_id = random_qu['id']
            try:
                prev_ques = visitedQuestion.objects.get(qid=rq_id)
                print("in try")
                continue
            except Exception as e:
                print(str(e))
                prev_ques = visitedQuestion()
                prev_ques.qid = random_qu['id']
                prev_ques.save()
                new_latest.append(random_qu)
                print("in except")

        context = {'Questions': new_latest}
        return Response(context)    

    













        #if len(final_ques)>0:

        #    latest = random.sample(final_ques,20)

         #   context = {'Questions':latest}
         
        #    return Response(context)
        #else:
         #   context = {'Questions':"NO question for U"}
          #  return Response(context)



        #context = {'Questions': final_ques}
        #return Response(context)


 
