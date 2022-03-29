from django.urls import path
from .api_views import test
from rest_framework.authtoken import views

urlpatterns = [
    path('test', test),
    path('auth', views.obtain_auth_token),
]
