from django.shortcuts import render
from django.http import HttpResponse
from .entities.test import TestForm

# Create your views here.

def test(request):
    if request.method == 'POST':
        print(request.POST)
        form = TestForm(request.POST)
        print(form.is_valid())
        form.save()
        return HttpResponse("Success")

    return HttpResponse("Failure")



