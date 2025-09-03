from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# import all models in OTS 
from OTS.models import *
# import template files 
from django.template import loader 

# Create your views here.

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())

def candidateRegistrationForm(request):
    res=render(request,'registration_form.html')
    return res

def cadidateRegistration(request):
    if request.mehtod=='POST':
        username=request.POST['username']
        #check if the user already exits
        if(len(Candidate.objects.filter(username=username))):
            userStatus=1
        else:
            candidate=Candidate()
            candidate.username=username
            candidate.password=request.POST['password']
            candidate.name.request.POST['name']
            candidate.save()
            userStatus=2
    else:
        userStatus=3 #Request method is not POSt
    context={
        'userStatus':userStatus
    }
    res=render(request,'registration.html',context)
    return res
def loginView(request):
    pass

def candidateHome(request):
    pass

def testPaper(request):
    pass

def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    pass

