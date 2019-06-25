from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
from news.translater import translate_hindi
wiki = "https://currentaffairs.gktoday.in"

page = urlopen(wiki)
soup = BeautifulSoup(page,features="html.parser")

content=soup.find_all("div",{"class":'post-content'})

title_list=[]
for x in content:
    title = x.find_all("a")

    for ti in title:
        text = ti.text
        if text=="":
           continue
        title_text=translate_hindi(text)
        title_list.append(title_text)
#print(len(title_list))
#print("title_list")
#print(title_list)
print("-----------------------------------------")


contents_list=[]

for x in content:
    news_text=translate_hindi(x.text)
    contents_list.append(news_text)
#print(list_text[2])
title_list=title_list[1:]
contents_list=contents_list[1:]
news_list =list(zip(title_list,contents_list))
for title,text in news_list:
    print(title)
    print(text)
    print("--------")
category=soup.find_all("p",{"class":'small-font'})

category_list=[]
for x in category:
    title = x.find_all("a")
    list2=[]
    for ti in title:
        text = ti.text
        if text=="":
           continue
        title_text=translate_hindi(text)
        list2.append(title_text)
    category_list.append(list2)
final_cate=[]
for cat in category_list:
   cate=cat[1]
   final_cate.append(cate)
final_category=final_cate[0:len(final_cate):2]
print(final_cate)
print(final_category)
print(len(final_category))
print(len(title_list))
print(len(contents_list))




























































# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import numpy as np
# from news.translater import translate_hindi
# wiki = "https://currentaffairs.gktoday.in/month/current-affairs-april-2019/"
#
# page = urlopen(wiki)
# soup = BeautifulSoup(page,features="html.parser")
#
# content=soup.find_all("div",{"class":'post-content'})
#
# title_list=[]
# for x in content:
#     title = x.find_all("a")
#
#     for ti in title:
#         text = ti.text
#         if text=="":
#            continue
#         title_text=translate_hindi(text)
#         title_list.append(title_text)
# #print(len(title_list))
# print("title_list")
# print(title_list)
# print("-----------------------------------------")
#
#
#
# final_list=[]
# for x in content:
#     news_text=x.find_all("p")
#     ul_text=x.find_all("ul")
#
#     list2=[]
#     for i in news_text:
#         gk=translate_hindi(i.text)
#         list2.append(gk)
#     final_list.append(list2)
# list5=[]
#
# for x in content:
#     ul_text = x.find_all("ul")
#     #print(ul_text)
#     list4=[]
#     for j in ul_text:
#         points =translate_hindi(j.text)
#         list4.append(points)
#     list5.append(list4)
#     #print(list4)
# d= np.array(final_list[1:])
# e=np.array(list5[1:])
# #print(type(e))
# #print(type(d))
# g=list(d)
# #print(final_list[1:])
# contents_list=[]
# for l in g:
#     list7=[]
#     for m in l:
#         list7.append(m)
#     contents_list.append(list7)
# #print(list8[0])
# #print("----------")
# #print(list8[1])
# title_list=title_list[1:]
# news_list =list(zip(title_list,contents_list))
# for title,text in news_list:
#     print(title)
#     print(text)
#     print("--------")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     # print(news_list)
#     # print(list(news_text))
# #print(final_list)
#
# #final=list(zip(title_list,final_list))
# #print(final)
# #for i in final:
#  #   print(i)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
