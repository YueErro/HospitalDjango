from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def index_view(request):
	context = {
		'ahora': timezone.now()
	}
	return render(request, 'home/index.html', context)

def contacto_view(request):
	return render(request,'home/contacto.html')