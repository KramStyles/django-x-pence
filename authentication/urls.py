from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# csrf_exempt is used to prevent django from securing the post request

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='auth-login'),
    path('register/', views.RegisterView.as_view(), name='auth-register'),

    path('validate_username/', csrf_exempt(views.UsernameValidationView.as_view()), name='auth-validate-username')
]