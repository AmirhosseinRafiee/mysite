from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
  return HttpResponse('This is home')

def about_view(request):
  return HttpResponse('This is about')

def contact_view(request):
  return HttpResponse('This is contact')
