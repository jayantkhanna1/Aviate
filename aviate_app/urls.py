
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('employeedashboard',views.employeedashboard,name='employeedashboard'),
    path('createnewjob',views.createnewjob,name='createnewjob'),
    path('oldjobs',views.oldjobs,name='oldjobs'),
    path('opensinglejobs',views.opensinglejob,name='opensinglejob'),
    path('searchjobs',views.searchjobs,name='searchjobs'),
    path('applyforjob',views.applyforjob,name='applyforjob'),
    path('createnewapplication',views.createnewapplication,name='createnewapplication'),
    path('candidates',views.candidates,name='candidates'),
    path('opensinglecandidate',views.opensinglecandidate,name='opensinglecandidate'),
]
