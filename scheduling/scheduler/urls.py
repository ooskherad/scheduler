from django.urls import path
from .api_views import *

app_name = "scheduler"
api_urlpatterns = [
    path('register', SchedulerRegistration.as_view()),
    path('create_service', CreateServiceView.as_view()),
    path('create_scheduler_service', CreateSchedulerServiceView.as_view()),
    path('services', GetAllServices.as_view()),
]
