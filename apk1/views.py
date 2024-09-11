from django.shortcuts import render
from celeryapp.celery import add
from celery.result import AsyncResult
# Create your views here.
def index(request):
 result = add.delay(10,20)
 return render(request,"Apk1\home.html", {'result':result})
def results(request, task_id):
    result = AsyncResult(task_id)
    return render(request, 'Apk1/result.html', {'result': result})

def about(request):
 return render(request,"Apk1\About.html")
def contact(request):
 return render(request,"Apk1\contact.html")