
from django.shortcuts import render
from .models import *
#from news.scarpdata import *
from django.contrib.auth.models import User, Group
#from news.theHinduEditorial import *
#from news.latest_Editorial import *
#
# Create your views here
import datetime
def home(request):

          try:
               #news_list =list(zip(title_list,contents_list,final_category))
               #for title, text, cat in news_list:
               news_list=list(zip(titless_list,hindi_titles,contents, hindi_contents,dateInserted_list))
               for title,h_title,text,h_text,da in news_list:
                    entries=News()
                    entries.title= title
                    entries.title_hindi=h_title
                    entries.hindi_news=h_text
                    entries.news_text= text
                    #print(text)
                    #entries.category= cat
                    entries.date=datetime.date.today()
                    #print(entries.date)
                    entries.save()
                    print("hiii")
               entry = News.objects.all().order_by('id').reverse()
                    #datewise = News.objects.filter(date__gte=datetime.date.today())
                    #for post in datewise:
                    #print(post.news_text)
               return render(request,'news/index.html', {'entry': entry})
          except:
               print("coming in except")
               entry = News.objects.all().order_by('id').reverse()
               return render(request, 'news/index.html',{'entry':entry})

def hindi(request):
     entry = News.objects.all().order_by('id').reverse()
     return render(request, 'news/index2.html', {'entry': entry})







