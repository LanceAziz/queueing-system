from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Client, Teller
from .serializer import ClientSerializer, TellerSerializer, TextSerializer
from datetime import datetime
from gtts import gTTS
import os
from django.conf import settings
from django.http import FileResponse, Http404

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
    user = request.user
    try:
        # Get the Teller associated with the authenticated user
        teller = Teller.objects.get(id=user.id)
    except Teller.DoesNotExist:
        return Response({"detail": "Teller not found for this user."}, status=status.HTTP_404_NOT_FOUND)

    today = datetime.now().date()
    client = Client.objects.filter(client_served__isnull=True, client_date=today, client_type=teller.type).order_by('client_num').first()

    if client:
        client.client_served = teller.num
        client.save()
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
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def speaker_audio(request):

    user = request.user
    today = datetime.now().date()
    
    try:
        # Get the Teller associated with the authenticated user
        teller = Teller.objects.get(id=user.id)
    except Teller.DoesNotExist:
        return Response({"detail": "Teller not found for this user."}, status=status.HTTP_404_NOT_FOUND)

    # Get the current client for this teller
    client = Client.objects.filter(client_audio=0,client_date=today, client_type=teller.type).order_by('client_num').first()
    client.client_audio = 1
    client.save()

    if client:
        # Generate text for the audio
        text = f"الْآنَ، عَمِيلٌ رَقْمُ {client.client_num}، شُبَّاكُ رَقْمُ {teller.num}"

        # Generate audio from text
        tts = gTTS(text=text, lang='ar')  # Example with Arabic language
        audio_filename = 'audio.mp3'
        audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)

        # Save the audio file
        with open(audio_path, 'wb') as f:
            tts.write_to_fp(f)

        # Return the audio file as a response
        try:
            return FileResponse(open(audio_path, 'rb'), content_type='audio/mpeg')
        except FileNotFoundError:
            raise Http404("Audio file not found")
    else:
        return Response({'error': 'No clients available for this teller'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_teller_info(request):
    user = request.user
    teller = Teller.objects.get(id=user.id)
    return Response({"detail": "Client updated successfully.","teller_num":teller.num,"teller_type":teller.type}, status=status.HTTP_200_OK)