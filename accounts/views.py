from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializers
from rest_framework.response import Response
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, Token
from rest_framework_simplejwt.models import TokenUser
# Create your views here.


class UserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(request.data)
            return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def delete(self,request):
        user = request.user 
        password = request.data.get('password')
        if password :
            if user.check_password(password):
                user.delete()
                return Response({'message': f'{user.username} Delete'})
            return Response({'message':'password different'})
        return Response({'message':'password not valid'})


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        profile =  get_object_or_404(User, username=username)
        serializer = UserSerializers(profile)
        return Response(serializer.data)

    def put(self, request, username):
        profile =  get_object_or_404(User, username=username)
        if profile.username == request.user.username:
            serializer = UserSerializers(profile, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        message = {'message': f'{profile.username} is different '}  
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
        
        

class logoutAPIView(APIView):
    def post(self, request):
        token = request.data.get('refresh')
        if token: 
            try:
                re_token = RefreshToken(token)
                re_token.blacklist()
                return Response({'message': 'logout'})
            except:
                return Response({'message': 'Already logout'})
        return Response({'message': 'not login'})

