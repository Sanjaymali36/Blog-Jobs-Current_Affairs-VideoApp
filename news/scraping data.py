

from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
from news.translater import translate_hindi
wiki = "https://currentaffairs.gktoday.in/month/current-affairs-april-2/"

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
print("title_list")
print(title_list)
print("-----------------------------------------")


contents_list=[]

for x in content:
    news_text=translate_hindi(x.text)
    contents_list.append(news_text)
#print(list_text[2])

news_list =list(zip(title_list[1:],contents_list[1:]))
for title,text in news_list:
    print(title)
    print(text)
    print("--------")




































