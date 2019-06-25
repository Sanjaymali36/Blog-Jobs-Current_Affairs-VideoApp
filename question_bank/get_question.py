import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from operator import is_not
url = "https://www.fresherslive.com/current-affairs/23-june-2019-quiz"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html,features="html.parser")
content=soup.find_all("div",{"class":'section group'})

question_list=[]



for x in content:                           #FOR QUESTION text
    j=x.find_all("div")
    for i in j[7:]:
        cont=i.find_all("div")
        for m in cont:
            cont1 = m.find_all("div")
            for n in cont1:
                kk=n.text
                question_list.append(kk)

            #question_list.append(ques)

#print(question_list)


final_ques_list=[]
correct_list=[]
exp_list=[]
for m in range(3,len(question_list)-2,9):
    ques=question_list[m]
    final_ques_list.append(ques)
    correct=question_list[m+5][18:]
    exp = question_list[m+7]
    correct_list.append(correct)
    exp_list.append(exp)
# print(final_ques_list)
# print(correct_list)
# print(exp_list)

option_list=[]                                   #FOR OPTION
for val in content:
    option=val.find_all("input")[3:]
    #print(option)
    option_list1=[]
    for j in option:
        #print(list(j))
        get_val =j["value"][2:]
        #print(get_val)
        option_list1.append(get_val)
    option_list.append(option_list1)

opt_list=[]
index = -1
for n in range(50):
    for k in option_list:
        opt_list.append(k[index:index+4])
        index+=4
opt_list = opt_list[1:]
options=[]
for m in opt_list:
    options.append(m)
# print(opt_list)
# print(options)
optionA=[i[0] for i in options if len(i)>1]
optionB=[i[1] for i in options if len(i)>1]
optionC=[i[2] for i in options if len(i)>1]
optionD=[i[3] for i in options if len(i)>1]
# print(optionA)
usedFor=[]

category=[]
lang=[]
source=[]
df = pd.DataFrame(list(zip(final_ques_list,correct_list,optionA,optionB,optionC,optionD,exp_list)),
               columns =['Question','correct','optA','optB','optC','optD','explanation'])

df['lang']="ENG"
df['source']=""
df['usedFor']=""
df['sectionType']="GK"
df['cat_num']="1.1"
df['direction']=""
# print("question coming")
# print(df)
df.to_csv("/home/bodhiai/Desktop/23_june.csv")
