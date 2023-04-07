from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProjectAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Project
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RoomAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Room
    serializer_class = RoomSerializer
    
    def get_queryset(self):
        queryset = Room.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Quality_issueAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Quality_issue
    serializer_class = Quality_issueSerializer
    
    def get_queryset(self):
        queryset = Quality_issue.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Safety_issueAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Safety_issue
    serializer_class = Safety_issueSerializer
    
    def get_queryset(self):
        queryset = Safety_issue.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Report_SafetyAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Report_Safety
    serializer_class = Report_SafetySerializer
    
    def get_queryset(self):
        queryset = Report_Safety.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Report_QualityAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Report_Quality
    serializer_class = Report_QualitySerializer
    
    def get_queryset(self):
        queryset = Report_Quality.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProjectAPIDetailView(APIView):
    def get_object(self, pk):
        try:
            project_list = Project.objects.get(id=pk)
            return project_list
        except project_list == "":
            sending = {
                    'error': 'Project does not found',
                    'error_code': 404,
                }
            return Response(sending ,status.HTTP_404_NOT_FOUND)
    
    def post(self, request, pk, format=None):
        if self.request.body == b'':
            project = self.get_object(pk)
            serializer = ProjectSerializer(project)
            responsing = {
                'name':serializer.data['name'],
                'description':serializer.data['description'],
                'category':serializer.data['category'],
                'quantity':serializer.data['quantity'],
                'unit':serializer.data['unit'],
                'price':serializer.data['price'],
                'image':serializer.data['image'],
                'owner':serializer.data['owner'],
                'is_available':serializer.data['is_available'],
             }
            return Response(responsing)
