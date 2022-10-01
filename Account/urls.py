from django.urls import path, include
from django.contrib import admin

from Account.views import RegisterView, LoginView, ChangePasswordView


urlpatterns = [
    path('register/', RegisterView.as_view() , name='register'),
    path('login/', LoginView.as_view() , name='login'),
    path('update-password/', ChangePasswordView.as_view() , name='update-password'),
]



