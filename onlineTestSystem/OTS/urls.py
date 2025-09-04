from django.urls import path 
# import all the OTS app View *
from OTS.views import *

app_name='OTS'

urlpatterns = [
    path('',welcome),

    path('new-candidate',candidateRegistrationForm, name='registrationForm'),

    path('store-candidate',cadidateRegistration,name='storeCandidate'),

    path('login',loginView,name='login'),

    path('home',candidateHome ,name='home'),

    path('test-paper',testPaper,name='testPaper'),

    path('calculate-result',calculateTestResult,name='calculateTest'),

    path('test-history',testResultHistory,name='testHistory'),

    path('result',showTestResult,name='result'),

    path('logout',logoutView,name='logout'),
]