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
    # Retrieve the Member object with the given id from the database
    mymember = Member.objects.get(id=id)
    # Prepare the context dictionary to pass data to the template
    context = {
        'mymember': mymember,
    }
    # Render the 'details.html' template with the provided context and return the HTTP response
    return render(request, 'details.html', context)

# Reformatted code for better readability

from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.template import loader

def my_first_html(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'myfirst.html', context)

def all(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'all_members.html', context)

def details(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember': mymember,
    }
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