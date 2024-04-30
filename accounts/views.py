from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializers
from rest_framework.response import Response
from .models import User
from rest_framework import status

# Create your views here.


@api_view(['POST'])
def signup(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.create(request.data)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    profile =  get_object_or_404(User, username=username)
    serializer = UserSerializers(profile)
    return Response(serializer.data)