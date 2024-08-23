from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Client, Teller
from .serializer import ClientSerializer, TellerSerializer
from datetime import datetime
from django.utils import timezone

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_clients(request):
    today = datetime.now().date()
    print(today)
    clients = Client.objects.all()
    serializeredData = ClientSerializer(clients, many=True)
    return Response(serializeredData.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_current_clients(request):
    today = datetime.now().date()
    print(today)
    clients = Client.objects.filter(client_date=today)
    serializeredData = ClientSerializer(clients, many=True)
    if (serializeredData):
        return Response(serializeredData.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_clients(request):
    data = request.data
    serializer = ClientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_clients(request):
    # Get the authenticated user
    user = request.user

    try:
        # Get the Teller associated with the authenticated user
        teller = Teller.objects.get(id=user.id)
    except Teller.DoesNotExist:
        return Response({"detail": "Teller not found for this user."}, status=status.HTTP_404_NOT_FOUND)

    today = timezone.now().date()

    client = Client.objects.filter(client_teller_id__isnull=True, client_date=today, client_type=teller.type).order_by('client_num').first()

    if client:
        # Update the `client_teller_id` for the first client to the authenticated teller
        client.client_teller_id = teller
        client.save()  # Save the updated client instance
        return Response({"detail": "Client updated successfully.","current_client":client.client_num,"teller_num":teller.num,"teller_type":teller.type}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "No clients available to update."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_teller(request):
    serializer = TellerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)