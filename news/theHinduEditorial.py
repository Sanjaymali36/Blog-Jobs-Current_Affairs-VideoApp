from urllib.request import urlopen
from bs4 import BeautifulSoup
from more_itertools import unique_everseen
from news.translater import translate_hindi

wiki1 = "https://www.thehindu.com/opinion/editorial/"
page = urlopen(wiki1)
soup = BeautifulSoup(page,features="html.parser")
links=soup.find_all("div",{"class":'Other-StoryCard'})
link_list1=[]
titless_list=[]
hindi_titles=[]


for x in links:               #for get all links
    l=x.a.get("href")

    title=x.a
    titles=title.text

    ti=titles.replace("\n","")                 #All titles
    news1 = translate_hindi(ti)

    titless_list.append(ti)
    hindi_titles.append(news1)
    link_list1.append(l)

final_content_list=[]
dateInserted_list=[]
hindi_news=[]
link_list1=link_list1[6:]
for wiki in link_list1:
    print(wiki)
    page = urlopen(wiki)
    soup = BeautifulSoup(page,features="html.parser")
    contents=soup.find_all("p",{"class":"drop-caps"})
    time = soup.find_all("span", {"class": "blue-color ksl-time-stamp"})
    hindi_text=[]
    content_list = []

    for x in contents:
        news=x.text
        news1=translate_hindi(news)
        hindi_text.append(news1)
        content_list.append(news)
    hindi_news.append(hindi_text)
    final_content_list.append(content_list)
    for t in time:
        timing=t.text
        timing=timing.replace("\n","")
        dateInserted_list.append(timing)
titless_list=titless_list[6:]
final_content_list=final_content_list[:]
contents=[]
for i in final_content_list:
    cont=i[0]

    contents.append(cont)
hindi_contents=[]
hindi_news=hindi_news[:]
for i in hindi_news:
    cont = i[0]
    # print(i)
    hindi_contents.append(cont)
dates=list(unique_everseen(dateInserted_list))
content_with_tiltes=list(zip(titless_list,final_content_list[0],dateInserted_list))
hindi_titles=hindi_titles[6:]
news_list=list(zip(titless_list,hindi_titles,contents, hindi_contents,dateInserted_list))
for title,h_title,text,h_text,da in news_list:
    print("start")
    print(title)
    print(text)
    print(h_title)
    print(h_text)
    print("------------------------------------")