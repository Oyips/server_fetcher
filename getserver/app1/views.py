from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return render(request,'section.html')

text=['this is section 1','this is section 2','this is section 3','this is section 4']

def section(request, num):
    if 1 <= num <= 4:
        return HttpResponse(text[num-1])
    else:
        return Http404('no such page')