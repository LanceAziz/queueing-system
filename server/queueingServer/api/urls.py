from django.urls import path
from .views import get_all_clients, create_clients, get_current_clients
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns=[
    # Client Endpoints
    path('clients/all', get_all_clients, name='get_all_clients'),
    path('clients/current', get_current_clients, name='get_current_clients'),
    path('clients/create/', create_clients, name='create_clients'),

    # Tellers Endpoints
    # path('tellers/signup/', create_teller, name='create_teller'),


    # # JWT Endpoints
    # path('token/', TokenObtainPairView.as_view()),
    # path('token/refresh/', TokenRefreshView.as_view()),
    # path('token/verify/', TokenVerifyView.as_view())
]