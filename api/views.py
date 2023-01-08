from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Simple_API
from .serializer import SimpleSerializer

# Create your views here.
@api_view(['GET'])
def getAPI(request):
    something=Simple_API.objects.all()
    serializer=SimpleSerializer(something, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postAPI(request):
    serializer=SimpleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

