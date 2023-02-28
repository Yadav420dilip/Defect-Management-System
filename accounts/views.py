from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm
from django.contrib import messages


class Account_Login(View):
    def get(self, request):
        forms = LoginForm
        return render(request, 'login.html', context={'forms': forms})

    def post(self, request):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(request, username=forms.cleaned_data.get('username'),
                                password=forms.cleaned_data.get('password'))

            if user is not None:
                login(request, user)
                return render(request, 'dashboard.html')
            else:
                messages.add_message(request=request, level=messages.INFO,
                                     message=' Login Failed! Enter the username and password correctly')

                return render(request, 'login.html', context={'forms': forms})
        else:
            messages.add_message(request=request, level=messages.INFO, message='Please enter the data in valid format.')
            return render(request, 'login.html', context={'forms': LoginForm(request.GET)})


def acc_logout(request):
    logout(request)
    return redirect('login')
