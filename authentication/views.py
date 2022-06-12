import json

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
            return JsonResponse({'username_error': 'Invalid username. Only alphanumerics allowed'}, status=400)
        return JsonResponse({'username_valid': True})
