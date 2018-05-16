from django.shortcuts import render
from django.http import Http404
from django import template
import time
from .models import MainDB
# Create your views here.

def index(request):
	all_MainDB=MainDB.objects.all()
	context={'all_MainDB': all_MainDB}
	return render(request, 'digi/test.html', context)