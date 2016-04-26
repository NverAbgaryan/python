from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound   
import datetime
# Create your views here.
def index(request, offset) :
	try :
		dt = datetime.datetime.now()
		offset = int(offset)
		if offset < -12 or offset > 12:
			 return HttpResponseNotFound("<h4>page Not found</h4>")
	 	delta = datetime.timedelta(hours = offset)

	 	dt += delta
		return HttpResponse(dt)
	except ValueError :
		return HttpResponseNotFound("<h4>page Not found</h4>")