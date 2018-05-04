# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def hello(request):
   return render(request, 'myapp/template/index.html', {})

def logged(request):
   return render(request, 'myapp/template/index.html', {'name':"Bob",'is_logged_in':True})

def map(request):
	return render(request, 'myapp/template/map.html', {'name':"Bob",'is_logged_in':True})

def dashboard(request):
	return render(request, 'myapp/template/dashboard.html', {'name':"Bob",'is_logged_in':True})

def prediction(request):
	return render(request, 'myapp/template/prediction.html', {'name':"Bob",'is_logged_in':True})

def predict(request):
	return render(request, 'myapp/template/predict.html', {'name':"Bob",'is_logged_in':True})