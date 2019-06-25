from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
import datetime
from .forms import DateWiseGKForm
from django.utils import timezone
def home(request):
    categories =Date_Category.objects.all().order_by('id').reverse()
    blogs = DateWiseGK.objects.all().order_by('updated_at').reverse()
    GK_categories=CategoryWise.objects.all().order_by('id').reverse()
    GK_blogs=CategoryWiseGK.objects.all().order_by('updated_at').reverse()
    return render(request,'gk_app/home.html', {'categories': categories,'blogs':blogs,'GK_categories': GK_categories,'GK_blogs':GK_blogs})

def category_topics(request, pk):
    category = get_object_or_404(Date_Category, pk=pk)
    topics = category.topics3.order_by('-last_updated')
    return render(request, 'gk_app/topics.html', {'category': category, 'topics': topics})
def categoryWise_topics(request, pk):
    category = get_object_or_404(CategoryWise, pk=pk)
    topics = category.topics4.order_by('-last_updated')
    GK_blogs = CategoryWiseGK.objects.all().order_by('updated_at').reverse()
    return render(request, 'gk_app/topics2.html', {'category': category, 'topics': topics ,'GK_blogs':GK_blogs})

def topic_posts(request, pk, topic_pk):
    topic =get_object_or_404(Topic, category__pk=pk, pk=topic_pk)
    topic.save()
    return render(request, 'gk_app/topic_posts.html', {'topic': topic})
def topic_posts2(request, pk, topic_pk):
    topic =get_object_or_404(TopicWise, category__pk=pk, pk=topic_pk)
    topic.save()
    print(topic)
    return render(request, 'gk_app/topic_posts2.html', {'topic': topic})



def create_blog(request):
    if request.method == "POST":
        form = DateWiseGKForm(request.POST)
        post = form.save()
        post.created_by = request.user
        post.updated_at = timezone.now()
        post.updated_by = request.user
        post.save()
        categories = Date_Category.objects.all()
        blogs = DateWiseGK.objects.all().order_by('updated_at')
        context ={'categories': categories,'blogs':blogs}
        return render(request,'gk_app/home.html',context)
    else:
        form = BlogForm()
    return render(request, 'gk_app/post_edit.html', {'form': form})

def comment(request):
    #comments = get_object_or_404(Comment, Blog__pk=pk, pk=Comment_pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        user = User.objects.all()
        user = user[0]
        new_comment = Comment()
        new_comment.user = user
        new_comment.date = datetime.datetime.now()
        new_comment.comment = body
        new_comment.save()
        comments = Comment.objects.all().order_by('id').reverse()
        categories = Category.objects.all().order_by('id').reverse()
        blogs = Blog.objects.all().order_by('updated_at').reverse()
        context = {'comments': comments}
        return render(request,'gk_app/home.html',{'comments': comments,'categories': categories,'blogs':blogs})

        #return redirect('topic_posts', pk=pk, Comment_pk=Comment_pk)
    else:
        form = BlogForm()
    return render(request, 'gk_app/reply_topic.html', {'form': form})


