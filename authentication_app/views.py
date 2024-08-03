from django.shortcuts import render

# Create your views here.
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class RegisterAPI(APIView):
    def post(self, request):
        _data = request.data
        serializer = RegisterSerializer(data = _data)
        
        if not serializer.is_valid():
            return Response({
                'message' : serializer.errors
            }, status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        
        return Response({
            'message':'Successfully Created'
        }, status=status.HTTP_201_CREATED)
        
        
class LoginAPI(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        _data = request.data
        serializer = LoginSerializer(data = _data)
        
        if not serializer.is_valid():
            return Response({
                'message':serializer.errors
            }, status=status.HTTP_404_NOT_FOUND)
            
        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])
        
        if not user:
            return Response({
                'message' : 'Invalid User'
            }, status= status.HTTP_404_NOT_FOUND)
            
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Login successfull', 'token':str(token),
            },status=status.HTTP_201_CREATED)
        

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS        


class UserListAPI(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    def get(self, request):
        queryset =  User.objects.all()
        username_serilizer = queryset.values_list('username', flat=True)
        return Response({'username':list(username_serilizer)})