import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:index'))
    
    return render(request, 'login.html', {})

def login_request(request):
    response_data = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if request.user.is_authenticated:
                response_data['result'] = '1'
            else:
                if user is not None:
                    response_data['result'] = '1'
                    response_data['message'] = ''
                    login(request, user)
                else:
                    response_data['result'] = '0'
                    response_data['message'] = 'Invalid Credentials'
        else:
            response_data['result'] = '0'
            response_data['message'] = 'Invalid Credentials'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

    # form = UserForm(request.POST)
    # if form.is_valid():
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         print("test")
    #         login(request, user)
    #         return redirect(reverse('dashboard:index'))
    #     else:
    #           form.add_error(None, 'Invalid credentials')
    # else:
    #      form = UserForm()

def user_logout(request):
    logout(request)
    return redirect('login_page')