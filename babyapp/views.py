from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import DataEntryForm, BabyEventForm
from .models import Baby, BabyEvent


# View to input new data
def input_data(request):
    if request.method == 'POST':
        # form = DataEntryForm(request.POST)
        form = BabyEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_data')  # Redirect to the page that shows all data entries
    else:
        # form = DataEntryForm()
        form = BabyEventForm()
    return render(request, 'input_data.html', {'form': form})

# View to display all data entries
def view_data(request):
    # data_entries = Baby.objects.all().order_by('-created_at_date')  # Order by the most recent first
    data_entries = BabyEvent.objects.all().order_by('-created_at_date') # Order by the most recent first
    return render(request, 'view_data.html', {'data_entries': data_entries})
# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('profile')  # Redirect to profile after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# View for user profile
def profile(request):
    return render(request, 'profile.html')
def home(request):
    # Retrieve recent entries
    # recent_entries = Baby.objects.all().order_by('-created_at_date')[:5]  # Get the latest 5 entries
    recent_entries = BabyEvent.objects.all().order_by('-created_at_date')[:5] # Get the latest 5 entries

    return render(request, 'home.html', {
        'recent_entries': recent_entries
    })