from django.urls import path
from .views import get_all_clients, create_clients, get_current_clients, register_teller, login_teller, test_token


urlpatterns=[
    # Client Endpoints
    path('clients/all', get_all_clients, name='get_all_clients'),
    path('clients/current', get_current_clients, name='get_current_clients'),
    path('clients/create/', create_clients, name='create_clients'),

    # Tellers Endpoints
    path('teller/register/', register_teller, name='register_teller'),
    path('teller/login/', login_teller, name='login_teller'),
    path('teller/test_token/', test_token, name='test_token'),

    # # Tokens Endpoints
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]