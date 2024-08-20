from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/dashboard'):  # adjust this to your dashboard URL
            token = request.COOKIES.get('token')
            if not token:
                return Response({"error": "Unauthorized"}, status=401)
            try:
                user = Token.objects.get(key=token).user
                request.user = user
            except Token.DoesNotExist:
                return Response({"error": "Invalid token"}, status=401)
        response = self.get_response(request)
        return response