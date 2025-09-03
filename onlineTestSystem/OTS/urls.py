from django.urls import path 
# import all the OTS app View *
from OTS.views import *

app_name='OTS'

urlpatterns = [
    path('',welcome),

    path('new-candidate',candidateRegistrationForm, name='registrationForm'),

    path('store-candidate',cadidateRegistration,name='storeCandidate'),

    path('login',loginView,name='login'),

    path('home',candidateHome),

    path('test-paper',testPaper),

    path('calculate-result',calculateTestResult),

    path('test-history',testResultHistory),

    path('result',showTestResult),

    path('logout',logoutView),
]