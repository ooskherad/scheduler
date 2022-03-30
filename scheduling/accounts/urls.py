from django.urls import path, include
from .api_views import UserCreationView, UserUpdateView, UserRegistrationVerifyOtpView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView

app_name = "accounts"
api_urlpatterns = [
    path('register', UserCreationView.as_view()),
    path('create', UserRegistrationVerifyOtpView.as_view()),
    path('user/<int:id>', UserUpdateView.as_view()),
    # path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth', views.obtain_auth_token),
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
]
