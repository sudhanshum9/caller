from django.shortcuts import render,redirect
from rest_framework import viewsets,filters,permissions as ps

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from django.forms.models import model_to_dict

from truecaller import serializers,models, permissions
from user import views,serializers as user_serializer
# Create your views here.
class GlobalDatabase(viewsets.ModelViewSet):
    """Handles reading all the data"""
    
    serializer_class = serializers.GlobalSerializer
    queryset = models.GlobalData.objects.all()
    
     

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating contacts feed items"""
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,ps.IsAuthenticatedOrReadOnly,ps.IsAuthenticated)
    #filter_backends = (filters.DjangoFilterBackend,SearchFilter, OrderingFilter)
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ('name','phoneno')
    #filter_fields = ('name','phoneno')
    ordering_fields = ('name','phoneno')
    def delete(self,request,pk=None):
        return Response({'message':'DELETE'})

class UserLoginApiView(ObtainAuthToken):
    """Handles login functionality"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class SpamViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating spam feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.SpamSerializer
    queryset = models.Spam.objects.all()
    permission_classes = (ps.IsAuthenticatedOrReadOnly,ps.IsAuthenticated)
    

class UserContactViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating contacts feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserContactSerializer
    queryset = models.UserContacts.objects.all()

    permission_classes = (permissions.UpdateOwnContact,ps.IsAuthenticatedOrReadOnly,ps.IsAuthenticated)
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ('phoneno')
    #filter_fields = ('name','phoneno')
    ordering_fields = ('phoneno')

    def get_queryset(self):
        return self.queryset.filter(user_profile_id=self.request.user)


    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


