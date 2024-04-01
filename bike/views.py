from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pulser(request):
    return HttpResponse('bike with best milage')