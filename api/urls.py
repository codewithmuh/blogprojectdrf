from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('account/', include('Account.urls')),
]



