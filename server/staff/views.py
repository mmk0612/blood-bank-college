from django.shortcuts import render, redirect

# Create your views here.

def staff_homepage(request):
    if not request.user.is_authenticated:
        return redirect('user-login')
    if not request.user.is_staff:
        return redirect('not-allowed')
    context = {}
    return render(request, 'staff/homepage.html', context)


def not_allowed(request):
    context = {}
    return render(request, 'staff/not-allowed.html', context)
