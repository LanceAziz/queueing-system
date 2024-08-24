from django.urls import path, include
from .views import get_all_clients, create_clients, get_current_clients, register_teller, edit_clients, speaker_audio, get_teller_info
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # Client Endpoints
    path('clients/all', get_all_clients, name='get_all_clients'),
    path('clients/current', get_current_clients, name='get_current_clients'),
    path('clients/create/', create_clients, name='create_clients'),
    path('clients/serve/', edit_clients, name='edit_clients'),
    path('clients/audio/', speaker_audio, name='speaker_audio'),

    # Tellers Endpoints
    path('teller/info', get_teller_info, name='get_teller_info'),
    path('teller/register/', register_teller, name='register_teller'),
    path('teller/login/', TokenObtainPairView.as_view(), name='login_teller'),
    path('teller/login/refresh', TokenRefreshView.as_view(), name='refresh_teller'),
    path('teller/api-auth', include("rest_framework.urls")),

    # # Tokens Endpoints
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)