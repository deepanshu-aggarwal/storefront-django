from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # pull data from database
    # transform data
    # send email

    return HttpResponse('hello world')
