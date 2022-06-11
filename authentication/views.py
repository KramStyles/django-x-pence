from django.shortcuts import render


def login(request):
    context = {
        'title': 'login'
    }
    return render(request, 'authentication/login.html', context)
