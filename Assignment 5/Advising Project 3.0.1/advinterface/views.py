from django.shortcuts import render, redirect, get_object_or_404
from .user_forms import UserForm
from .forms import MajorRequirementsForm
from .models import UserProfile, Advisor
from django.contrib.auth.models import User



def index(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']

        # Check if a user with the given email already exists
        existing_user = User.objects.filter(username=email).first()
        if existing_user:
            # If user exists, redirect or handle as needed
            # You might want to show an error message or redirect back to the registration page
            return render(request, 'registration_error.html')

        # Create a new user
        user = User.objects.create_user(
            username=email,
            email=email,
            password='dummy'
        )

        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        user_profile = form.save(commit=False)
        user_profile.user = user
        user_profile.save()

        return redirect('classes', user_id=user_profile.id)
  else:
    form = UserForm()

  return render(request, 'index.html', {'form': form})


def classes(request, user_id):
  user_profile = get_object_or_404(UserProfile, id=user_id)
  advisor = Advisor.objects.get(pk=1)

  if request.method == 'POST':
      major_requirements_form = MajorRequirementsForm(request.POST, instance=user_profile)
      if major_requirements_form.is_valid():
          # Process the form data as needed
          pass
  else:
      major_requirements_form = MajorRequirementsForm(user_profile=user_profile)

  return render(
      request, 'classes.html', {
          'user_profile': user_profile,
          'advisor': advisor,
          'major_requirements_form': major_requirements_form,
      })

def submit(request):
  return render(request, 'submit.html')
