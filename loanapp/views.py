from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CreateUserForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import CreateUser


# Create your views here.
def index(requests):
    return render(requests, 'loanapp/index.html')


# user register
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print('valid form')
            username = request.POST['email'].split('@')[0]
            form.instance.username = username
            messages.success(request, 'Account Created Successfully')
            form.save()

            return redirect('register')
        else:
            print('invalid form')
    return render(request, 'loanapp/register.html', {'form': form})


# userlogin
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                user = authenticate(username=uname, password=pw)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfully loggedin!!")
                    # return HttpResponseRedirect('/profile/')
                    return redirect('profile')
        else:
            fm = AuthenticationForm()
        return render(request, 'loanapp/login.html', {'form': fm})
    else:
        return redirect('profile')


def userprofile(request):
    if request.user.is_authenticated:
        data = CreateUser.objects.all()
        return render(request, 'loanapp/profile.html', {'data': data})
    else:
        return redirect('login')


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Changed Successfully')
                return redirect('profile')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'loanapp/changepass.html', {'form': fm})
    else:
        return redirect('login')
