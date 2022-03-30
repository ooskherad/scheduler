from django.urls import path, include
from .api_views import UserCreationView, UserUpdateView, UserRegistrationVerifyOtpView
from rest_framework.authtoken import views

app_name = "accounts"
api_urlpatterns = [
    path('register', UserCreationView.as_view()),
    path('create', UserRegistrationVerifyOtpView.as_view()),
    path('user/<int:id>', UserUpdateView.as_view()),
    path('auth', views.obtain_auth_token),
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
]
