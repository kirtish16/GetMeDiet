from django.urls import path
from MyApp import views as v

urlpatterns = [
path('',v.index,name=''),
path('bmi',v.bmi,name='bmi'),
path('dietplan',v.dietplan,name='dietplan'),
path('contactus',v.contactus,name='contactus'),
]