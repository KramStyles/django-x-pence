from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        context = {
            'title': 'login'
        }
        return render(request, 'authentication/login.html', context)
