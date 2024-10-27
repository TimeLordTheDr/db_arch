from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
# django.template import loader

from .models import Member

def my_first_html(request):
    # return HttpResponse("Hello world!")
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
   
    # return render(request, 'myfirst.html', context)
    mymembers = Member.objects.all().values()
  # template = loader.get_template('all_members.html')
    context = {
    'mymembers': mymembers,
    }
    
    return render(request, 'myfirst.html', context)
    

from django.template import loader


def all(request):
  mymembers = Member.objects.all().values()
  # template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'all_members.html', context)


def details(request, id):
  mymember = Member.objects.get(id=id)
  # template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'details.html', context)


def main(request):
  # template = loader.get_template('main.html')
  # return HttpResponse(template.render())
  return render(request, 'main.html')

def testing(request):
  # template = loader.get_template('template.html')
  # mydata = Member.objects.filter(first_name='New').values()
  mydata = Member.objects.all().order_by('-first_name', '-salary').values()
  context = {
    'mymembers': mydata,
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'template.html', context)