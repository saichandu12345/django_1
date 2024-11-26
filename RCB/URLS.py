from django.urls import path

from RCB.views import *

urlpatterns=[
    path('Captain/',Captain,name='Captain'),
]