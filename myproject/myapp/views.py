# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def hello(request):
   return render(request, 'myapp/template/index.html', {})

def logged(request):
   return render(request, 'myapp/template/index.html', {'name':"Jessica",'is_logged_in':True})

def library(request):
	return render(request, 'myapp/template/library.html', {'name':"Jessica",'is_logged_in':True})

def predict(request):
	return render(request, 'myapp/template/predict.html', {'name':"Jessica",'is_logged_in':True})

def history(request):
	return render(request, 'myapp/template/history.html', {'name':"Jessica",'is_logged_in':True})

def prediction(request):
	return render(request, 'myapp/template/prediction.html', {'name':"Jessica",'is_logged_in':True})