from urllib.request import urlopen
from bs4 import BeautifulSoup

from functools import partial
url = "http://www.freejobalert.com/government-jobs/"

page = urlopen(url)
soup = BeautifulSoup(page,features="html.parser")

content=soup.find_all("div",{"class":'post'})
content_list2=[]
for i in content:
    rows = i.find_all('tr')
    links = i.find_all('a')
    #print(links)
    content_list1=[]
    for row in rows:
        row_td = row.find_all('td')

        content_list=[]
        for k in row_td:
            kkk=k.a
            #print(kkk)

            kk=k.text
            content_list.append(kk)
        content_list1.append(content_list)
    content_list2.append(content_list1)


link_list=[]
for i in content:
    rows = i.find_all('tr')
    links = i.find_all('a')
    #o=[x for x in links if x is not "None"]
    for l in links[16:]:
        demo=l.get('href')
        if l.string is not None:
            link=l.get('href')
            link_list.append(link)


    # content_list1=[]
    # for row in rows:
    #     row_td = row.find_all('td')
    #
    #     content_list=[]
    #     for k in row_td:
    #         kkk=k.a
    #         print(kkk)









list11=[]
for i in content_list2:
    for a in i[8:]:
        list11.append(a)
#print(len(list11))
# print(type(list11))
# print(list11)
print(len(link_list))
date_list=[]
department_list=[]
post_name_list=[]
qualifiction_list=[]
AdvtNo_list=[]
LastDate_list=[]
for i in list11:
    if len(i) > 3:
        date = i[0]
        department=i[1]
        post_name=i[2]
        qualifiction=i[3]
        AdvtNo=i[4]
        LastDate=i[5]

        date_list.append(date)
        department_list.append(department)
        post_name_list.append(post_name)
        qualifiction_list.append(qualifiction)
        AdvtNo_list.append(AdvtNo)
        LastDate_list.append(LastDate)
print(len(date_list))
# print(date_list)
# print(department_list)
# print(post_name_list)
# print(qualifiction_list)
# print(AdvtNo_list)
# print(LastDate_list)
job_contents=list(zip(date_list,department_list,post_name_list,qualifiction_list,AdvtNo_list,LastDate_list,link_list))
job_contents1=list(zip(date_list,department_list,post_name_list,qualifiction_list,AdvtNo_list,LastDate_list,link_list))
for i in job_contents:
    print(i)
# print("---------------------------------------------------------")
# for a,b,c,d,e,f,g in job_contents1:
#     print(a)
