from django.urls import path 
# import all the OTS app View *
from OTS.views import *

urlpatterns = [
    path(' ',welcome),
    path('new-candidate',candidateRegistrationForm),
    path('store-candidate',cadidateRegistration),
    path('login',loginView),
    path('home',candidateHome),
    path('test-paper',testPaper),
    path('calculate-result',claculateTestResult),
    path('test-history',testResultHistory),
    path('result',showTestResult),
    path('logout',logoutView),
]