# advinterface/views.py
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def profile_creation(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Process the form data and save to the database
            # For example, create a UserProfile instance and save it
            # Make sure to handle saving related classes (communication_classes, mathematics_class, etc.)
            # based on your model structure
            # Redirect to a success page after saving
            return render(request, 'advinterface/submit.html')
    else:
        form = UserProfileForm()

    return render(request, 'advinterface/index.html', {'form': form})

def submission_successful(request):
    return render(request, 'advinterface/submit.html')
