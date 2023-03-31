from django.shortcuts import render

TEMPLATE_HOMEPAGE = "homepage.html"
TEMPLATE_EVENTS = "events.html"
TEMPLATE_ABOUT_US = "about-us.html"
TEMPLATE_DONATE_BLOOD = "donate-blood.html"
TEMPLATE_REQUEST_BLOOD = "request-blood.html"
TEMPLATE_DONATIONS = "donations.html"
TEMPLATE_VOLUNTEER = "volunteer.html"

# Create your views here.
def homepage(request):
    context = {}
    return render(request, TEMPLATE_HOMEPAGE, context)

def events(request):
    context = {}
    return render(request, TEMPLATE_EVENTS, context)

def about_us(request):
    context = {}
    return render(request, TEMPLATE_ABOUT_US, context)

def donate_blood(request):
    context = {}
    return render(request, TEMPLATE_DONATE_BLOOD, context)

def request_blood(request):
    context = {}
    return render(request, TEMPLATE_REQUEST_BLOOD, context)

def donations(request):
    context = {}
    return render(request, TEMPLATE_DONATIONS, context)

def volunteer(request):
    context = {}
    return render(request, TEMPLATE_VOLUNTEER, context)

from api.forms import RequestBloodForm
TEMPLATE_TEST = "test.html"

def test(request):
    context = {"form_html": RequestBloodForm().as_p()}
    return render(request, TEMPLATE_TEST, context)
