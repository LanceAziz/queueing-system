from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Client, Teller
from .serializer import ClientSerializer, TellerSerializer
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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
    teller = get_object_or_404(Teller, username=data['username'])
    if not teller.check_password(data['password']):
        return Response({"detail": "No Teller matches the given query."}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=teller)
    serializer = TellerSerializer(instance=teller)
    response = JsonResponse({"message": "Login successful"})
    response.set_cookie(
        key='auth_token',
        value=token.key,
        max_age=3600,  # Cookie expiry time in seconds
        httponly=True,  # Makes the cookie inaccessible to JavaScript
    )
    
    return response
    # response = Response({"teller": serializer.data})
    # response.set_cookie(
    #     key='token', 
    #     value=token, 
    #     httponly=True,  # This makes the cookie inaccessible to JavaScript for security reasons.
    #     samesite='Lax',  # Adjust this based on your needs, it helps prevent CSRF attacks.
    #     secure=True if request.is_secure() else False,  # Send the cookie over HTTPS if the request is secure.
    #     # max_age=60 * 60 * 24,
    # )
    # return response

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
 return Response({
     "username":request.user.username,
     "teller_num":request.user.teller_num,
     "teller_type":request.user.teller_type
     })