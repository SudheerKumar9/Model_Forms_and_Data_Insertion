from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):

    TMFO=TopicModelForm()
    s={'TMFO':TMFO}
    if request.method=='POST':
        TMFOD=TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse('<center><h1>Topic Data is Submitted SuccessFully</h1></center>')

    return render(request,'insert_topic.html',s)


def insert_webpage(request):

    WPMFO=WebpageModelForm()
    d={'WPMFO':WPMFO}
    if request.method=='POST':
        WPMFOD=WebpageModelForm(request.POST)
        if WPMFOD.is_valid():
            WPMFOD.save()
            return HttpResponse('<center><h1>Webpage Data is Submitted SuccessFully</h1></center>')
            

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):

    ARMFO=AccessRecordModelForm()
    d={'ARMFO':ARMFO}
    if request.method=='POST':
        ARMFOD=AccessRecordModelForm(request.POST)
        if ARMFOD.is_valid():
            ARMFOD.save()
            return HttpResponse('<center><h1>AccessREcord Data is Submitted SuccessFully</h1></center>')
            

    return render(request,'insert_accessrecord.html',d)