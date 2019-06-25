# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
import datetime
from .forms import BlogForm
from django.utils import timezone
def home(request):
    categories =Category.objects.all().order_by('id').reverse()
    blogs = Blog.objects.all().order_by('updated_at').reverse()
    entries = latest.objects.filter(status=latest.PUBLISHED).order_by('last_update').reverse()
    #entries = latest.objects.all().order_by('last_update').reverse()
    return render(request,'blog/index2.html', {'categories': categories,'blogs':blogs,'entries': entries})

def category_topics(request, pk):
    category = get_object_or_404(Category, pk=pk)
    topics = category.topics.order_by('-last_updated')
    return render(request, 'blog/topics.html', {'category': category, 'topics': topics})

def topic_posts(request, pk, topic_pk):
    topic =get_object_or_404(Topic, category__pk=pk, pk=topic_pk)
    topic.save()
    return render(request, 'blog/topic_posts.html', {'topic': topic})

def entry(request, slug):
    blog_entry = get_object_or_404(latest, slug=slug)
    return render(request, 'blog/title.html', { 'blog': blog_entry })




def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        post = form.save()
        post.created_by = request.user
        post.updated_at = timezone.now()
        post.updated_by = request.user
        post.save()
        categories = Category.objects.all()
        blogs = Blog.objects.all().order_by('updated_at')
        context ={'categories': categories,'blogs':blogs}
        return render(request,'blog/home.html',context)
    else:
        form = BlogForm()
    return render(request, 'blog/post_edit.html', {'form': form})

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
        return render(request,'blog/home.html',{'comments': comments,'categories': categories,'blogs':blogs})

        #return redirect('topic_posts', pk=pk, Comment_pk=Comment_pk)
    else:
        form = BlogForm()
    return render(request, 'blog/reply_topic.html', {'form': form})
"""
def get_title(request,pk):

    pk1=request.POST.get('pk')
    print(pk1)

    if request.method == 'POST':

        blogs = Blog.objects.get(pk=pk1)
        return render(request,'blog/title.html',{"blogs":blogs})
"""
def get_title(request,pk):
    print(request.POST.get('pk'),False)
    title_id=request.POST['pk']
    print(title_id)
    print ('hiii')
    if request.method == 'POST':
        blogs=get_object_or_404(Blog,pk=pk)
        #blogs = Blog.objects.get(id=title_id)
        return render(request,'blog/title.html',{"blogs":blogs})


   
