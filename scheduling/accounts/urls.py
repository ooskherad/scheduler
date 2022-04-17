from django.urls import path, include
from .api_views import UserRegistrationView, UserUpdateView, UserRegistrationVerifyOtpView, UserLogin, UserProfile
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = "accounts"
api_urlpatterns = [
    path('register', UserRegistrationView.as_view()),
    path('verify_otp', UserRegistrationVerifyOtpView.as_view()),
    path('user/<int:id>', UserUpdateView.as_view()),
    path('profile', UserProfile.as_view(), name='profile'),
    # path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth', views.obtain_auth_token),
]

urlpatterns = [
    path('login', UserLogin.as_view()),

]
