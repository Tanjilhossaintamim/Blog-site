from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def signup(request):
    form = forms.CustomSignUpForm()

    if request.method == 'POST':
        form = forms.CustomSignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:login'))
    dic = {
        'form': form,
    }

    return render(request, 'login/signup.html', context=dic)


def login_user(request):
    form = AuthenticationForm()

    dic = {
        'form': form,

    }

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('login:profile'))

    return render(request, 'login/login.html', context=dic)


@login_required
def profile(request):
    dic = {}
    return render(request, 'login/profile.html', context=dic)


@login_required
def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))


@login_required
def edit_user(request):
    form = forms.EditUser(instance=request.user)
    update = False
    if request.method == 'POST':
        form = forms.EditUser(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = forms.EditUser(instance=request.user)
            update = True

    return render(request, 'login/edit_user.html', context={'form': form, 'update': update})


@login_required
def password_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))
    return render(request, 'login/password_change.html', context={'form': form})


@login_required
def add_profile_pic(request):
    form = forms.ProfilePictureForm()
    if request.method == 'POST':
        form = forms.ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()

    return render(request, 'login/add_profile_pic.html', context={'form': form})

@login_required
def change_profile_pic(request):
    current_user = request.user.user_all_profile
    form = forms.ProfilePictureForm(instance=current_user)
    if request.method == 'POST':
        form = forms.ProfilePictureForm(
            request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))

    return render(request, 'login/add_profile_pic.html', context={'form': form})
