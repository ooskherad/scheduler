from accounts.urls import api_urlpatterns
from django.urls import path, include

api_urls = [
    path('accounts/', include(api_urlpatterns))
]