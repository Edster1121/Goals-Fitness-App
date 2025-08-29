from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from members.forms import SignUpForm


def login_user(request):
    return render(request, 'registration/login.html', {})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after registration
            return redirect('index')  # redirect to main page
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

