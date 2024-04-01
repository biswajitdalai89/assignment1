from django.urls import path
from aeroplane.views import *
app_name='something'

urlpatterns = [
    path('indigo/',indigo,name='indigo.html')
]