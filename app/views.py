from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}


    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic is inserted successfully')
        else:
            return HttpResponse('data is not valid')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WF=WebpageForm()
    d={'WF':WF}


    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('webpage is inserted successfully')
        else:
            return HttpResponse('data is not entered properly')
    return render(request,'insert_webpage.html',d)

def insert_Access(request):
    AFO=AccessForm()
    d={'AFO':AFO}

    if request.method=='POST':
        AFD=AccessForm(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('Access data is inserted properly')
        else:
            return HttpResponse('data not given properly check again')
    return render(request,'insert_Access.html',d)


