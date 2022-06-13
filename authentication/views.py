import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .utils import Functions

func = Functions()


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
        return JsonResponse({'_error': msg}, status=status_code)


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not func.emailCheck(email):
            msg = 'Invalid email. Use correct email format'
            status_code = 400
        elif User.objects.filter(email=email).exists():
            msg = 'Email already in use!'
            status_code = 409
        else:
            return JsonResponse({'message': 'valid'})
        return JsonResponse({'_error': msg}, status=status_code)


class PasswordValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        password = data['password']

        if len(password) < 4:
            msg = 'Password is too short'
            status_code = 400
        else:
            if func.validate_password(password):
                return JsonResponse({'message': 'valid'})
            else:
                msg = 'Password must contain al'
                status_code = 409
        return JsonResponse({'_error': msg}, status=status_code)
