from accounts.urls import api_urlpatterns as accounts_urls
from scheduler.urls import api_urlpatterns as scheduer_urls
from django.urls import path, include

api_urls = [
    path('accounts/', include(accounts_urls)),
    path('scheduler/', include(scheduer_urls)),
]