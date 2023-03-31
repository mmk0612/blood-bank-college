from django.shortcuts import render

TEMPLATE_HOMEPAGE = "homepage.html"
TEMPLATE_EVENTS = "events.html"

# Create your views here.
def homepage(request):
    context = {}
    return render(request, TEMPLATE_HOMEPAGE, context)

def events(request):
    context = {}
    return render(request, TEMPLATE_EVENTS, context)
