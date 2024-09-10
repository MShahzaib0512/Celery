from django.shortcuts import render
from celeryapp.celery import add
# Create your views here.
def index(request):
 print(add.delay(10,20))
 return render(request,"Apk1\home.html")
def about(request):
 return render(request,"Apk1\About.html")
def contact(request):
 return render(request,"Apk1\contact.html")