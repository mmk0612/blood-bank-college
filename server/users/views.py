from django.shortcuts import render
from .forms import ProfileCreationForm

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/register.html')
    else:
        form = ProfileCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
