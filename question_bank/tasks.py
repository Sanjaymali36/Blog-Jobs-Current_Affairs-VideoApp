import pandas as pd
import numpy as np
from .views import *
import pickle
import json
from .models import *
from django.http import Http404

def add_to_database_questions_text(sheet_link,school,production=False, explanation_quest=False):
    for sh in sheet_link:
        if production:
            df = \
                pd.read_csv('/home/ubuntu/blog_project/question_bank/question_data/' + sh, error_bad_lines=False)
        else:
            df = \
                pd.read_csv('/home/ubuntu/blog_project/question_bank/question_data/' + sh, error_bad_lines=False)

        quests = []
        optA = []
        optB = []
        optC = []
        optD = []
        optE = []
        right_answer = []
        quest_category = []
        temp = []
        used_for = 'English siel'
        lang = "English"
        source = "SIEL"
        quest_text = df['Question']
        optA = df['optA']
        num_a = len(optA)
        optB = df['optB']
        optC = df['optC']
        optD = df['optD']
        try:
            direction = df['direction']
        except:
            direction = ['lll']

        try:
            optE = df['optE']
        except:
            optE = ['lll']
        sectionType = "English"
        quest_category = df['cat_num']
        for i in df['correct']:
            ichanged = str(i).replace(u'\\xa0', u' ')
            ichanged2 = ichanged.replace('Answer', ' ')
            ichanged3 = ichanged2.replace('Explanation', ' ')

            if 'a' in ichanged.lower() or '1' in ichanged.lower():
                right_answer.append(1)
            elif 'b' in ichanged.lower() or '2' in ichanged.lower():
                right_answer.append(2)
            elif 'c' in ichanged.lower() or '3' in ichanged.lower():
                right_answer.append(3)
            elif 'd' in ichanged.lower() or '4' in ichanged.lower():
                right_answer.append(4)
            elif 'e' in ichanged.lower() or '5' in ichanged.lower():
                right_answer.append(5)
        print('%s num quest text' % len(quest_text))
        print('%s optA' % len(optA))
        print('%s optB' % len(optB))
        print('%s optC' % len(optC))
        print('%s optD' % len(optD))
        try:
            print('%s optE' % len(optE))

        except Exception as e:
            print(str(e))
        print('%s correct answers' % len(right_answer))
        print('%s number of categories' % len(quest_category))
        for ind in range(len(optA)):
            try:
                if str(optE[ind]).lower() == 'noopt':
                    print('only four options')
                    if direction[0] != 'lll':
                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], optD[ind], None, None,
                                        right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '4', direction[ind])
                    else:
                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], optD[ind], None, None,
                                        right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '4')

                else:
                    if direction[0] != 'lll':
                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], optD[ind], optE[ind],
                                        None, right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '5', direction[ind])
                    else:
                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], optD[ind], optE[ind],
                                        None, right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '5')


            except Exception as e:
                print(str(e))
                if str(optD[ind]).lower() == 'noopt':
                    print('only 3 options')
                    if direction[0] != 'lll':
                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], None, None, None,
                                        right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '3', direction[ind])
                    else:
                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], None, None, None,
                                        right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '3')

                else:
                    if direction[ind] != 'lll':
                        print("Going in else of --if-- of four option")
                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], optD[ind], None, None,
                                        right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '4', direction[ind])
                    else:

                        write_questions(school, quest_text[ind], optA[ind], optB[ind], optC[ind], optD[ind], None, None,
                                        right_answer[ind], quest_category[ind], None, sectionType, lang, used_for,
                                        source, '4')

                    print('most 4 options')


def add_to_database_questions(sheet_link,school, production=False, onlyImage=False, fiveOptions=False,explanation_quest=False):
    for sh in sheet_link:
        if production:
            df = \
                pd.read_csv('/home/ubuntu/blog_project/question_bank/question_data/' + sh,
                            error_bad_lines=False)
        else:
            df = \
                pd.read_csv('/home/ubuntu/blog_project/question_bank/question_data/' + sh,
                            error_bad_lines=False)

        quests = []
        optA = []
        optB = []
        optC = []
        optD = []
        optE = []
        right_answer = []
        quest_category = []
        temp = []
        optA = df['optA']
        optB = df['optB']
        optC = df['optC']
        optD = df['optD']

        try:
            direction = df['direction']
        except:
            direction = len(optD) * ['None']
        try:
            difficulty = df['difficulty']
        except:
            difficulty = len(optD) * ['None']
        used_for = df['usedFor']
        lang = df['lang']
        source = df['usedFor']
        if onlyImage:
            images = df['QuestionLink']
        else:
            quest_text = df['Question']
        sectionType = df['sectionType']
        # direction = df['Direction']
        try:
            exp = df['explanation']
        except:
            exp = len(optD) * ['None']
        quest_category = df['category']
        for i in df['correct']:
            ichanged = str(i).replace(u'\\xa0', u' ')
            ichanged2 = ichanged.replace('Answer', ' ')
            ichanged3 = ichanged2.replace('Explanation', ' ')

            if 'a' in ichanged.lower() or '1' in ichanged.lower():
                right_answer.append(1)
            elif 'b' in ichanged.lower() or '2' in ichanged.lower():
                right_answer.append(2)
            elif 'c' in ichanged.lower() or '3' in ichanged.lower():
                right_answer.append(3)
            elif 'd' in ichanged.lower() or '4' in ichanged.lower():
                right_answer.append(4)
            elif 'e' in ichanged.lower() or '5' in ichanged.lower():
                right_answer.append(5)
        if fiveOptions:
            optE = df['optE']

        if onlyImage:
            print('%s num images' % len(images))
        else:
            print('%s num quest text' % len(quest_text))
        print('%s optA' % len(optA))
        print('%s optB' % len(optB))
        print('%s optC' % len(optC))
        print('%s optD' % len(optD))
        try:
            print('%s optE' % len(optE))
        except Exception as e:
            print(str(e))
        print('%s correct answers' % len(right_answer))
        print('%s number of categories' % len(quest_category))
        # print('%s languages ' %len(lang))
        print('%s sources' % len(source))
        print('%s sheet ' % sh)
        try:
            print('{} exp link'.format(len(exp)))
        except Exception as e:
            print('explanation not found')

        for ind in range(len(optA)):
            if onlyImage and fiveOptions:
                write_questions(school, None, optA[ind], optB[ind], optC[ind], optD[ind], optE[ind], images[ind],
                                right_answer[ind], quest_category[ind], exp[ind], sectionType[ind], str(lang[ind]),
                                used_for[ind], source[ind], fouroptions='5', direction
                                =direction[ind], difficulty=difficulty[ind])
            else:

                # if onlyImage:
                write_questions(school, None, optA[ind], optB[ind], optC[ind], optD[ind], None, images[ind],
                                right_answer[ind], quest_category[ind], exp[ind], sectionType[ind], str(lang[ind]),
                                used_for[ind], source[ind], fouroptions='4', direction
                                =direction[ind], difficulty=difficulty[ind])
            # else:
            #    write_questions(school,quest_text,optA[ind],optB[ind],optC[ind],optD[ind],None,None,right_answer[ind],quest_category[ind],None,sectionType[ind],lang[ind],used_for[ind],source[ind],direction[ind],fouroptions='3')


def \
        write_questions(school, question, optA, optB, optC, optD, optE, image, correctOpt, questCategory, exp,
                        sectionType, lang, used_for, source, fouroptions, direction=False, replace=False,
                        difficulty=None):
    print('{} this is the exp link'.format(exp))
    try:
        old_question = SSCquestions.objects.get(text=question)
        return
    except:
        if replace:
            quest = SSCquestions.objects.filter(text=question)
            for n, qu in enumerate(quest):
                for num, ch in enumerate(qu.choices_set.all()):
                    print(num)
                    if num + 1 == correctOpt:
                        ch.predicament = 'Correct'
                    else:
                        ch.predicament = 'Wrong'
                    ch.save()

        else:

            school = School.objects.filter(name=school)
            if fouroptions == '4':
                all_options = [optA, optB, optC, optD]
            elif fouroptions == '3':
                all_options = [optA, optB, optC]
            elif fouroptions == '5':
                all_options = [optA, optB, optC, optD, optE]


            else:
                try:
                    if optE:
                        print('Found optE in final')
                        if math.isnan(optE):
                            all_options = [optA, optB, optC, optD]
                        else:
                            all_options = [optA, optB, optC, optD, optE]
                    else:
                        all_options = [optA, optB, optC, optD, optE]
                except Exception as e:
                    print(str(e))
                    all_options = [optA, optB, optC, optD, optE]
            new_questions = SSCquestions()
            new_questions.language = lang

            new_questions.usedFor = used_for

            if source:
                new_questions.source = source

            new_questions.tier_category = '1'
            new_questions.max_marks = int(1)
            new_questions.negative_marks = 0.0
            print('{} is the section cateogry'.format(sectionType))
            if sectionType == 'English':
                new_questions.section_category = 'English'
            elif sectionType == 'Reasoning':
                new_questions.section_category = 'General-Intelligence'
            elif sectionType == 'Maths':
                new_questions.section_category = 'Quantitative-Analysis'
            elif sectionType == 'GK':
                new_questions.section_category = 'General-Knowledge'
            elif sectionType == 'groupxen':
                new_questions.section_category = 'Defence-English'
            elif sectionType == 'groupxphy':
                new_questions.section_category = 'Defence-Physics'
            elif sectionType == 'groupxmath':
                new_questions.section_category = 'GroupX-Maths'
            elif sectionType == 'groupgk':
                new_questions.section_category = 'Defence-GK-CA'
            elif sectionType == 'jeeMaths10':
                new_questions.section_category = 'MathsIITJEE10'
            elif sectionType == 'jeeMaths11':
                new_questions.section_category = 'MathsIITJEE11'
            elif sectionType == 'jeeMaths12':
                new_questions.section_category = 'MathsIITJEE12'
            elif sectionType == 'jeePhysics10':
                new_questions.section_category = 'PhysicsIITJEE10'
            elif sectionType == 'jeePhysics11':
                new_questions.section_category = 'PhysicsIITJEE11'
            elif sectionType == 'jeePhysics12':
                new_questions.section_category = 'PhysicsIITJEE12'
            elif sectionType == 'jeeChemistry10':
                new_questions.section_category = 'ChemistryIITJEE10'
            elif sectionType == 'jeeChemistry11':
                new_questions.section_category = 'ChemistryIITJEE11'
            elif sectionType == 'inorganic_chem_JEE':
                new_questions.section_category = 'ChemistryIITJEE12'
            elif sectionType == 'locopilot_electrical':
                new_questions.section_category = 'ElectricalLocoPilot'
            elif sectionType == 'locopilot_fitter':
                new_questions.section_category = 'FitterLocoPilot'
            elif sectionType == 'general_science':
                new_questions.section_category = 'General-Science'
            elif sectionType == 'locopilot_diesel':
                new_questions.section_category = 'LocoPilot_Diesel'
            elif sectionType.strip() == 'cat_quant':
                new_questions.section_category = 'CAT_Quantitative_Aptitude'
            elif sectionType.strip() == 'loco_civil':
                new_questions.section_category = 'Civil_Loco_Pilot_Tech'
            elif sectionType.strip() == 'ssc_electrical':
                new_questions.section_category = 'SSC_Electronics1'
            elif sectionType.strip() == 'BasicScienceLocopilot':
                new_questions.section_category = 'Basic-Science'
            elif sectionType.strip() == 'EnvironmentStudyLocopilot':
                new_questions.section_category = 'Environment-Study'
            elif sectionType.strip() == 'EngineeringDrawingLocopilot':
                new_questions.section_category = 'Engineering-Drawing'

            # if question != None:
            #    new_questions.text = str(question)
            print('%s direction, %s question' % (direction, question))
            if direction != 'None' and question is None:
                new_questions.text = str(direction)
            elif question != None and direction:
                new_questions.text = str(direction) + '\n' + str(question)
            elif direction == None or direction == '' or direction == 'lll':
            
                new_questions.text = str(question).replace("nan","")

            elif question and direction == False:
                new_questions.text = str(question).replace("nan","")

            new_questions.topic_category = str(questCategory)
            if direction:
                try:
                    if direction != 'None':
                        print('%s inside' % direction)
                        print(type(direction))
                        direct = Comprehension()
                        direct.picture = direction
                        direct.save()
                    else:
                        print('%s outside' % direction)
                except:
                    pass
            if difficulty:
                if difficulty != 'None':
                    new_questions.diffculty_category = difficulty
                else:
                    print('direction but something wrong')
            if image:
                new_questions.picture = image
                # try:
                #    new_questions.comprehension = direct
                # except:
                #    pass
            new_questions.save()
            for sch in school:
                new_questions.school.add(sch)
            # for j in range(1,9):
            #    if questCategory == str(j):
            #        mn = questCategory + '.'+'1'
            #        new_questions.topic_category = str(mn)
            #        new_questions.topic_category = str(mn)
            #        new_questions.save()
            #    else:
            #        new_questions.topic_category = str(questCategory)
            #        new_questions.save()
            # print(new_questions.topic_category)
            for n, i in enumerate(all_options):
                new_choices = Choices()
                new_choices.sscquest = new_questions
                if 'https:' in str(i):
                    new_choices.picture = str(i)
                else:
                    itext = str(i).replace('[', '')
                    itext2 = itext.replace(']', '')
                    itext3 = itext2.replace(')', '')
                    itext4 = itext3.replace(u'\\xa0', u' ')
                    itext5 = itext4.replace('\"', '')
                    new_choices.text = itext5
                # if 'https:' in str(exp):
                #    pass
                # else:
                #    exptext = str(exp).replace('[','')
                #    exptext2 = exptext.replace(']','')
                #    exptext3 = exptext2.replace(u'\\xa0',u' ')
                #    exptext4 = exptext3.replace('\"','')
                if correctOpt == n + 1:
                    new_choices.predicament = 'Correct'
                    # if 'https:' in str(exp):
                    new_choices.explanationPicture = exp
                    # else:
                    #    new_choices.explanation = exptext4
                else:
                    new_choices.predicament = 'Wrong'
                new_choices.save()
