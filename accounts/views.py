from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserSerializers
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def signup(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.create(request.data)
        return Response(serializer.data)