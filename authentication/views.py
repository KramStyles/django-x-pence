from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        context = {
            'title': 'login'
        }
        return render(request, 'authentication/login.html', context)


class RegisterView(View):
    def get(self, request):
        context = {
            'title': 'Registration'
        }
        return render(request, 'authentication/register.html', context)
