from urllib.request import urlopen
from bs4 import BeautifulSoup
from more_itertools import unique_everseen
from news.translater import translate_hindi
wiki1 = "https://www.thehindu.com/opinion/editorial/"

page = urlopen(wiki1)

soup = BeautifulSoup(page,features="html.parser")


links=soup.find_all("div",{"class":'ES2-100x4-text1 hover-icon'})

link_list1=[]


titless_list=[]
hindi_titles=[]
for x in links:               #for get all links
    l=x.a.get("href")
    #print(l)
    title=x.a
    titles=title.text

    ti=titles.replace("\n","")
    titles = translate_hindi(ti)
    titless_list.append(ti)
    hindi_titles.append(titles)
    link_list1.append(l)

final_content_list=[]
dateInserted_list=[]
hindi_news=[]
for wiki in link_list1:
    #print(wiki)

    page = urlopen(wiki)
    #print(page)
    soup = BeautifulSoup(page,features="html.parser")
    #print(soup)
    contents=soup.find_all("p",{"class":"drop-caps"})
    time = soup.find_all("span", {"class": "blue-color ksl-time-stamp"})
    #print(titles)
    content_list = []
    hindi_text=[]
    for x in contents:
        #texts1=x.text
        texts=translate_hindi(x.text)
        hindi_text.append(texts)
        content_list.append(x.text)
    hindi_news.append(hindi_text)
    final_content_list.append(content_list)
    for t in time:
        timing=t.text
        timing=timing.replace("\n","")
        dateInserted_list.append(timing)
#print(dateInserted_list)
titless_list=list(unique_everseen(titless_list))
final_content_list=final_content_list
contents=[]
for i in final_content_list:
    cont=i[0]
    contents.append(cont)
hindi_contents= []
for i in hindi_news:
    cont=i[0]
    hindi_contents.append(cont)
print(hindi_news)
print(hindi_titles)
# #print(contents)
# for i in contents:
#     print(i)
#     print("----------------")
#print(final_content_list)
#print(titless_list)
#print(contents)
# print ("Total titles {}".format(len(titless_list)))
# print ("Total Editorial {}".format(len(final_content_list)))
#
# dates=list(unique_everseen(dateInserted_list))
# print(len(dates))