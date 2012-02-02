# Create your views here.
from django.shortcuts import render

def home(request):
	render('itfit',request)