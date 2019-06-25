

from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
#from .video import *


"""
def home(request):

    try:
        video_list = list(zip(title_list,video_url,thumbnail_list,published_list))

        for i in video_list:
            entries = Video()
            entries.video_title = i[0]
            entries.content = i[1]
            entries.link1 = i[2]
            entries.save()
            print("hiii")
        entry = Video.objects.all().order_by('id').reverse()

        return render(request, 'videoapp/homepage111.html', {'entries': entry})
    except:
        print("coming in except")
        entry = Video.objects.all().order_by('id').reverse()
        return render(request, 'videoapp/homepage111.html', {'entries': entry})

"""
def home(request):

    try:
        video_list = list(zip(title_list,video_url,thumbnail_list,published_list))

        for i in video_list:
            entries = Entry()
            entries.title = i[0]
            entries.summary = i[1]

            entries.link1 = i[2]

            #entries.slug=i.pk
            slug_str = "%s" % (i[0].lower())
            entries.slug = slugify(slug_str)
            entries.created_by=request.user
            entries.save()
            print("hiii")
        entry = Entry.objects.all().order_by('id').reverse()

        return render(request, 'videoapp/homepage111.html', {'entries': entry})
    except:
        print("coming in except")
        entry = Entry.objects.all().order_by('id').reverse()
        return render(request, 'videoapp/homepage111.html', {'entries': entry})


def entry(request,id):
    blog_entry = get_object_or_404(Entry,id=id)
    return render(request, 'videoapp/entry.html', { 'entry': blog_entry })






# def home(request):
#     categories =Category.objects.all().order_by('id').reverse()
#     blogs = Video_Content.objects.all().order_by('updated_at').reverse()
#     entries = Entry.objects.filter(status=Entry.PUBLISHED).order_by('last_update').reverse()
#
#     return render(request,'videoapp/homepage.html', {'categories': categories,'blogs':blogs,'entries': entries })

def category_topics(request,pk):
    category = get_object_or_404(Category, pk=pk)
    topics = category.topics1.order_by('-last_updated').reverse()
    print("hiiii")
    return render(request, 'videoapp/topics.html', {'category': category, 'topics': topics})
def topic_posts(request, pk, topic_pk):
    topic =get_object_or_404(Topic, category__pk=pk, pk=topic_pk)
    topic.save()
    return render(request, 'videoapp/topic_posts.html', {'topic': topic})
def get_title(request,id):
    print(request.POST.get('id'),False)
    title_id=request.POST['id']
    print(title_id)
    print ('hiii')
    if request.method == 'POST':
        #blogs=get_object_or_404(Blog,id=pk)
        blogs = Blog.objects.get(id=title_id)
        return render(request,'videoapp/title.html',{"blogs":blogs})
