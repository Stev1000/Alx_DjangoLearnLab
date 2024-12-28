from django.shortcuts import render, redirect
from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileUpdateForm

# Registration view using CustomUserCreationForm
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use CustomUserCreationForm here
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')  # After successful registration, redirect to login
    else:
        form = CustomUserCreationForm()  # Use CustomUserCreationForm here
    return render(request, 'register.html', {'form': form})

# Profile view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = ProfileUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = ProfileUpdateForm(instance=request.user)

    return render(request, 'registration/profile.html', {'u_form': u_form})
