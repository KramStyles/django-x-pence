import json

from django.contrib.auth.models import User
from django.http import JsonResponse
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


# REQUESTS

class UsernameValidationView(View):
    def post(self, request):
        print('hello', request.body)
        data = json.loads(request.body)
        username = data['username']

        if not username.strip().isalnum():
            msg = 'Invalid username. Only alphanumerics allowed'
            status_code = 400
        elif User.objects.filter(username=username).exists():
            msg = 'User already exists'
            status_code = 409
        else:
            return JsonResponse({'username_valid': True})
        return JsonResponse({'username_error': msg}, status=status_code)
