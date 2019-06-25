from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
import datetime
#from jobs.jobsContent import *
from django.utils import timezone
def home(request):
    categories =Location.objects.all().order_by('id').reverse()
    blogs = LoctionWiseJobs.objects.all().order_by('updated_at').reverse()
    GK_categories=Departments.objects.all().order_by('id').reverse()
    GK_blogs=DepartmentWiseJobs.objects.all().order_by('updated_at').reverse()
    return render(request,'jobs/home.html', {'categories': categories,'blogs':blogs,'GK_categories': GK_categories,'GK_blogs':GK_blogs})




# def home(request):
#     print("hiiiiii")
#     try:
#         job_contents = list(zip(date_list, department_list, post_name_list, qualifiction_list, AdvtNo_list, LastDate_list, link_list))
#
#         for a, b, c, d, e, f, g in job_contents:
#             entries = Jobs()
#
#             entries.job_department = b
#             entries.job_title = c
#             entries.qualification = d
#             entries.notification = e
#
#             # entries.last_date = i[5]
#             entries.apply_link = g
#             # print(entries.date)
#             entries.save()
#             print("hiii")
#         entry = Jobs.objects.all().order_by('id').reverse()
#         return render(request, 'jobs/home.html', {'entries': entry})
#     except:
#         print("coming in except")
#         entry = Jobs.objects.all().order_by('id').reverse()
#         return render(request, 'jobs/home.html', {'entries': entry})








def category_topics(request, pk):
    category = get_object_or_404(Location, pk=pk)
    topics = category.topics8.order_by('-last_updated')
    return render(request, 'jobs/topics.html', {'category': category, 'topics': topics})
def categoryWise_topics(request, pk):
    category = get_object_or_404(Departments, pk=pk)
    topics = category.topics9.order_by('-last_updated')
    GK_blogs = DepartmentWiseJobs.objects.all().order_by('updated_at').reverse()
    return render(request, 'jobs/topics2.html', {'category': category, 'topics': topics ,'GK_blogs':GK_blogs})

def topic_posts(request, pk, topic_pk):
    topic =get_object_or_404(Location_Category, category__pk=pk, pk=topic_pk)
    topic.save()
    return render(request, 'jobs/topic_posts.html', {'topic': topic})
def topic_posts2(request, pk, topic_pk):
    topic =get_object_or_404(Department_sub_Category, category__pk=pk, pk=topic_pk)
    topic.save()
    print(topic)
    return render(request, 'jobs/topic_posts2.html', {'topic': topic})





