from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from .models import Client, Teller
from .serializer import ClientSerializer, TellerSerializer
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET'])
def get_all_clients(request):
    today = datetime.now().date()
    print(today)
    clients = Client.objects.all()
    serializeredData = ClientSerializer(clients, many=True)
    return Response(serializeredData.data)

@api_view(['GET'])
def get_current_clients(request):
    today = datetime.now().date()
    print(today)
    clients = Client.objects.filter(client_date=today)
    serializeredData = ClientSerializer(clients, many=True)
    if (serializeredData):
        return Response(serializeredData.data)

@api_view(['POST'])
def create_clients(request):
    data = request.data
    serializer = ClientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_teller(request):
    data = request.data
    serializer = TellerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        teller = Teller.objects.get(username=data['username'])
        teller.set_password(data['password'])
        teller.save()
        token = Token.objects.create(user=teller)
        return Response({"token:": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_teller(request):
    data = request.data
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return Response({"detail": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    print(data)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = JsonResponse({
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "teller_num": data.get("num"),
            "teller_type": data.get("type")
        })

        # Set the cookies
        response.set_cookie(
            key='access',
            value=access_token,
            httponly=True,
            secure=False,  # Set to True in production with HTTPS
            max_age=5 * 60,  # 5 minutes for access token
            samesite='Strict',
        )
        response.set_cookie(
            key='refresh',
            value=refresh_token,
            httponly=True,
            secure=False,  # Set to True in production with HTTPS
            max_age=60 * 60 * 24,  # 24 hours for refresh token
            samesite='Strict',
        )

        return response
    else:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({
        "username": request.user.username,
        "teller_num": request.user.num,
        "teller_type": request.user.type
    })