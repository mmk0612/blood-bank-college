from django.shortcuts import render, redirect
from .forms import Profile, ProfileCreationForm, ProfileLoginForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def user_register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('homepage')

    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProfileCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


from django.contrib.auth.views import LoginView
def user_login(request):
    return LoginView.as_view(
            template_name='users/login.html',
            authentication_form=ProfileLoginForm,
            next_page='homepage',
            ) (request)

def user_logout(request):
    if request.user.is_authenticated:
        messages.info(request, 'You have been logged out')
        logout(request)
    return redirect('homepage')
