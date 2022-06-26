import json

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .utils import Functions
from lib import email_txt

func = Functions()


class LoginView(View):
    def get(self, request):
        context = {
            'title': 'login'
        }
        return render(request, 'authentication/login.html', context)

    def post(self, request):
        context = {
            'title': 'Sign In'
        }
        messages.success(request, 'Hello and good day')
        messages.error(request, 'Hello and bahd day')
        return render(request, 'authentication/login.html', context)


class RegisterView(View):
    def get(self, request):
        context = {
            'title': 'Registration'
        }
        return render(request, 'authentication/register.html', context)


class VerifyView(View):
    def get(self, request, encoded_email):
        try:
            decoded_email = func.decode_email(encoded_email)
            user = User.objects.get(email=decoded_email)
            user.is_active = True
            user.save()
            context = {
                'title': 'User Verified'
            }
            messages.success(request, 'User is Verified')
        except (TypeError, KeyError, OverflowError, User.DoesNotExist, UnicodeDecodeError) as err:
            context = {
                'title': 'User Not Verified'
            }
            messages.error(request, f'User not Verified: {str}')

        return render(request, 'authentication/login.html', context)


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
                msg = 'Password must contain symbols, digits,  upper & lower characters'
                status_code = 409
        return JsonResponse({'_error': msg}, status=status_code)


class SignUpView(View):
    def post(self, request):
        data = request.POST

        password = data['password']
        email = data['email']
        username = data['username']

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.is_active = False

        # Send verification email
        encoded = func.encode_email(email)
        url = f"{request.scheme}://{get_current_site(request).domain}/verify/{encoded}"

        data = {
            'email_subject': 'X-Pence :: Email Verification Mail',
            'email_body': email_txt.email_template(email, url),
            'to_email': email
        }
        print(email, url)
        func.send_email(data)

        user.save()

        return JsonResponse({'_msg': 'Account created Successfully'}, status=200)
