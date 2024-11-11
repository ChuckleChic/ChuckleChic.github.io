from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import DiaryEntryForm
from .models import DiaryEntry
from textblob import TextBlob
from django.contrib.auth.decorators import login_required

from .models import DiaryEntry

# Home Page
@login_required
def home(request):
    entries = DiaryEntry.objects.all().order_by('-created_at')  # Sort entries by created_at
    return render(request, 'myapp/home.html', {'entries': entries})


# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to homepage after successful login
        else:
            # If user doesn't exist, display error and suggest registration
            messages.error(request, "User does not exist. Please register first.")
            return render(request, 'myapp/login.html')

    return render(request, 'myapp/login.html')

# User Registration View
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)  # Log the user in automatically after registration
            
            # Display success message
            messages.success(request, "Registration successful! You are now logged in.")
            
            return redirect('home')  # Redirect to homepage after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'myapp/register.html', {'form': form})

# Add Diary Entry
@login_required
def add_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            
            # Perform sentiment analysis using TextBlob
            blob = TextBlob(content)
            sentiment = 'Positive' if blob.sentiment.polarity > 0 else 'Negative' if blob.sentiment.polarity < 0 else 'Neutral'

            # Create and save the diary entry
            entry = form.save(commit=False)
            entry.user = request.user
            entry.sentiment = sentiment  # Save the sentiment analysis result
            entry.save()
            
            return redirect('home')  # Redirect to homepage after saving
    else:
        form = DiaryEntryForm()
    
    return render(request, 'myapp/add_entry.html', {'form': form})

# Viewing individual diary entry details
def entry_detail(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)
    return render(request, 'myapp/entry_detail.html', {'entry': entry})


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'  # Specify your template here

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the homepage or any other page after logout
