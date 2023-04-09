from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#Views for Flow Django app

#having issues with this *v*

def flow(request):
	#return HttpResponse("im back")
	template = loader.get_template('home.html')
	return HttpResponse(template.render())
