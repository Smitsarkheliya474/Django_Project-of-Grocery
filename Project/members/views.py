from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Grocery_Items

def home(request):
    return render(request,"home3.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def insertdata(request):
    a = request.POST['firstname']
    b = request.POST['lastname']
    c = request.POST['email']
    d = request.POST['password']
    enter = Grocery_Items(firstname = a, lastname = b, email = c, password = d)
    enter.save()
    return HttpResponseRedirect(reverse('login'))

def checkdata(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        password1 = request.POST['password']
        
        try:
            user = Grocery_Items.objects.get(email=email1,password=password1) 
            if user.email == email1 and user.password == password1:
                return render(request,'home3.html')
            else:
                return render(request, 'error.html')
        except:
            pass
    return render(request, 'error.html')

def table(request):
    details = Grocery_Items.objects.all().values()
    template = loader.get_template('table.html')
    context = {
        'details' : details
    }
    return HttpResponse(template.render(context, request))

def delete(id):
    member = Grocery_Items.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('table'))

def update(request, id):
    mymember = Grocery_Items.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
      'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updatedata(request, id):
    a = request.POST['fname']
    b = request.POST['lname']
    c = request.POST['eml']
    d = request.POST['pswrd']
    member = Grocery_Items.objects.get(id=id)
    member.firstname = a
    member.lastname = b
    member.email = c
    member.password = d
    member.save()
    return HttpResponseRedirect(reverse('table'))