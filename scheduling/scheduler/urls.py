from django.urls import path
from .api_views import SchedulerRegistration

app_name = "scheduler"
api_urlpatterns = [
    path('register', SchedulerRegistration.as_view()),
]
