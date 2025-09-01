from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# import all models in OTS 
from OTS.models import *
# import template files 
from django.template import loader 

# Create your views here.

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(request)

def candidateRegistrationForm(request):
    pass

def cadidateRegistration(request):
    pass

def loginView(request):
    pass

def candidateHome(request):
    pass

def testPaper(request):
    pass

def claculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    pass

