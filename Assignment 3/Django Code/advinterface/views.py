from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import StudentRegistrationForm, StudentLoginForm, CustomAuthenticationForm
from .models import Major, Advisor

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'form': form, 'error': 'Email is already taken'})
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            # Create User and Student instances
            user = User.objects.create_user(username=email, email=email, password=form.cleaned_data.get('password1'), first_name=first_name, last_name=last_name)
            student = form.save(commit=False)
            student.user = user
            student.save()
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = CustomAuthenticationForm()

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        email = form.request.POST.get('email')
        password = form.request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            form = CustomAuthenticationForm(request)
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    student = request.user.student
    advisor = Advisor.objects.filter(major=student.major).first()
    return render(request, 'dashboard.html', {'student': student, 'advisor': advisor})
