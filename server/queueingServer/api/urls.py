from django.urls import path
from .views import get_clients, create_clients

urlpatterns=[
    path('clients/', get_clients, name='get_clients'),
    path('clients/create/', create_clients, name='create_clients'),
]