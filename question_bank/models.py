from django.contrib.auth.models import User
from django.db import models
import datetime

class School(models.Model):
    category_choices = (('School', 'School'), ('SSC', 'SSC'))
    name = models.CharField(max_length=200)
    pincode = models.IntegerField()
    category = models.CharField(max_length=10, choices=
    category_choices, null=True, blank=True)
    logo = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class SSCquestions(models.Model):
    ch = 1
    tp = 1
    topic_choice = []
    topic_choice2 = []
    for ch in range(1,70):
        for tp in range(1,10):
            topic_choice.append(str(ch)+'.'+str(tp))
            topic_choice2.append(str(ch)+'.'+str(tp))
    tp_choice = list(zip(topic_choice,topic_choice2))
    topic_choice = tuple(tp_choice)

    max_marks = models.IntegerField(default= 2)
    negative_marks =\
    models.DecimalField(max_digits=2,decimal_places=2,default=0.25)
    tier_choices = (('1','Tier1'),('2','Tier2'),('3','Tier3'))
    usedFor_choices =\
    (('SSC','SSC'),('Aptitude','Aptitude'),('Groupx','Groupx'),('Groupy','Groupy'),('RPSC','RPSC'),('RAS','RAS'),('IITJEE','IITJEE'))
    language_choices = (('English','English'),('Hindi','Hindi'),('Bi','Bi'))
    section_choices = \
        (('General-Intelligence','General-Intelligence'),('General-Knowledge','General-Knowledge')
         ,('Quantitative-Analysis','Quantitative-Analysis'),('English','English')
         ,('Defence-English','Defence-English'),('Defence-Physics','Defence-Physics')
         ,('GroupX-Maths','GroupX-Maths'),('Defence-GK-CA','Defence-GK-CA')
         ,('MathsIITJEE10','MathsIITJEE10'),('MathsIITJEE11','MathsIITJEE11')
         ,('MathsIITJEE12','MathsIITJEE12'),('ChemistryIITJEE10','ChemistryIITJEE10')
         ,('ChemistryIITJEE11','ChemistryIITJEE11'),('ChemistryIITJEE12','ChemistryIITJEE12')
         ,('PhysicsIITJEE10','PhysicsIITJEE10'),('PhysicsIITJEE11','PhysicsIITJEE11')
         ,('PhysicsIITJEE12','PhysicsIITJEE12'),('Design and analysis of algorithm','Design and analysis of algorithm')
         ,('ElectricalLocoPilot','ElectricalLocoPilot'),('FitterLocoPilot','FitterLocoPilot')
         ,('General-Science','General-Science'),('LocoPilot_Diesel','LocoPilot_Diesel'),
        ('CAT_Quantitative_Aptitude','CAT_Quantitative_Aptitude'),('Civil_Loco_Pilot_Tech','Civil_Loco_Pilot_Tech'),
        ('SSC_Electronics1','SSC_Electronics1'),('Basic-Science','Basic-Science'),('Environment-Study','Environment-Study'),('Engineering-Drawing','Engineering-Drawing'),
        ('Physics_NEET','Physics_NEET'),('Chemistry_NEET','Chemistry_NEET'),('Botony_NEET','Botony_NEET'),('Physics_IIT','Physics_IIT'),('Maths_IIT','Maths_IIT'),
        ('Chemistry_IIT','Chemistry_IIT'))
    diffculty_choices = (('easy','easy'),('medium','medium'),('hard','hard'))
    text = models.TextField(blank=True,null=True)
    tier_category = models.CharField(max_length=20,choices = tier_choices)
    section_category  = models.CharField(max_length=70,choices = section_choices)
    diffculty_category = models.CharField(max_length = 10,choices =
                                          diffculty_choices,null=True,blank=True)
    topic_category = models.CharField(max_length=5,choices = topic_choice)
    #school = models.ManyToManyField(School)
    picture = models.URLField(max_length=500,null=True,blank=True)
    usedFor = models.CharField(max_length=30,null=True,blank=True)
    source = models.CharField(max_length= 50,null=True,blank=True)
    dateInserted = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    language = models.CharField(max_length = 20,null=True,blank=True )
    #concepts = models.ManyToManyField(Concepts)

    def __str__(self):
        return str(self.id)

class Choices(models.Model):
    class Meta:
        ordering = ['pk']
    res_choice = (('Correct','Correct'),('Wrong','Wrong'),('Not decided','Not decided'))
    predicament = models.CharField(max_length= 30, choices = res_choice)
    #quest = models.ForeignKey(Questions,blank=True,null=True)
    sscquest = models.ForeignKey(SSCquestions,on_delete=models.CASCADE,blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    picture = models.URLField(null=True,blank=True)
    explanation = models.TextField(null=True,blank=True)
    explanationPicture= models.URLField(null=True,blank=True)
    def __str__(self):
        if self.text != None:
            return self.text[:50]
        else:
            return self.picture

class visitedQuestion(models.Model):
    qid=models.IntegerField()
    test_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.qid)

