
from django.shortcuts import render
from .models import *
#from news.scarpdata import *
#from django.contrib.auth.models import User, Group
from django.http import Http404, HttpResponse
# Create your views here
import datetime
from .tasks import *
from .get_question import *
def home(request):
    # entry = Questions.objects.all().order_by('id').reverse()
    # return render(request, 'question/index.html',{'entry':entry})
    sheet_links =['23_june.csv']
    add_to_database_questions(sheet_links, 'BodhiAI', production=True, onlyImage=True)
    add_to_database_questions_text(sheet_links, 'BodhiAI', production=True)
    return HttpResponse("Successs")
