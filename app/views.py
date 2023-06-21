from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('the topic is inserted')

def insert_webpage(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter a name')
    u=input('enter a url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('the webpage data is inserted')

def insert_accessrecord(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter a name')
    u=input('enter a url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter date')
    at=input('enter a author')
    ARO=AccessRecord.objects.get_or_create(name=WO,date=d,author=at)[0]
    ARO.save()
    return HttpResponse('the acessrecord data is inserted')

