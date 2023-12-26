from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def login(request):
  next = request.GET.get('next')
  if request.user.is_authenticated:
    if request.GET.get('next') != None:
      return redirect(request.GET.get('next'))
    messages.warning(request, 'you are in your account!')
    return redirect('/')
  elif request.method == 'POST':
    user_input = request.POST.get('username')
    try:
      username = User.objects.get(email=user_input).username
    except User.DoesNotExist:
      username = user_input
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      auth_login(request, user)
      messages.success(request, 'Login successful.')
      if request.GET.get('next') != None:
        return redirect(request.GET.get('next'))
      return redirect('/')
    messages.warning(request, 'Login failed. Please check your username and password.')
  return render(request, 'accounts/login.html', {'next': next})


@login_required
def logout(request):
  auth_logout(request)
  messages.success(request, "You've been successfully logged out.")
  return redirect('/')

def signup(request):
  if request.user.is_authenticated:
    messages.warning(request, 'you are in your account!')
    return redirect('/')
  elif request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'User created.')
      return redirect('/accounts/login')
    else:
      for e in form.errors.values():
        messages.warning(request, e)
  else:
    form = UserCreationForm()
  return render(request, 'accounts/signup.html', {'form': form})