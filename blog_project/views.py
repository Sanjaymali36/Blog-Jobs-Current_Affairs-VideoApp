
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    context = {'hello':'hello'}
    return render(request,'blog/homepage.html',context)
