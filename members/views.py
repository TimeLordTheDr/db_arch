from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# django.template import loader

def members(request):
    # return HttpResponse("Hello world!")
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
    return render(request, 'myfirst.html')