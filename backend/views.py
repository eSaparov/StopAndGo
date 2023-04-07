from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from rest_framework.authentication import TokenAuthentication

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProjectAPIListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    model = Project
    serializer_class = ProjectSerializer
    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RoomAPIListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    model = Room
    serializer_class = RoomSerializer
    
    def get_queryset(self):
        queryset = Room.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Quality_issueAPIListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    model = Quality_issue
    serializer_class = Quality_issueSerializer
    
    def get_queryset(self):
        queryset = Quality_issue.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Safety_issueAPIListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    model = Safety_issue
    serializer_class = Safety_issueSerializer
    
    def get_queryset(self):
        queryset = Safety_issue.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Report_SafetyAPIListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    model = Report_Safety
    serializer_class = Report_SafetySerializer
    
    def get_queryset(self):
        queryset = Report_Safety.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Report_QualityAPIListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    model = Report_Quality
    serializer_class = Report_QualitySerializer
    
    def get_queryset(self):
        queryset = Report_Quality.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProjectAPIDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        
        project_list = Project.objects.get(id=pk)
        print(project_list)
        if project_list == "":
            sending = {
                    'error': 'Project does not found',
                    'error_code': 404,
                }
            return Response(sending ,status.HTTP_404_NOT_FOUND)
        else: return project_list
    
    def get(self, pk):
        if self.request.body == b'':
            project = self.get_object(pk)
            serializer = ProjectSerializer(project)
            print(project.name)
            print(serializer.data)
            responsing = {
                'name':serializer.data['name'],
                'fullname':serializer.data['fullname'],
             }
            return Response(responsing)

class RoomAPIDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        
        room_list = Room.objects.get(id=pk)
        print(room_list)
        if room_list == "":
            sending = {
                    'error': 'Project does not found',
                    'error_code': 404,
                }
            return Response(sending ,status.HTTP_404_NOT_FOUND)
        else: return room_list
    
    def get(self, pk):
        if self.request.body == b'':
            room = self.get_object(pk)
            serializer = RoomSerializer(room)
            print(room.name)
            print(serializer.data)
            responsing = {
                'index':serializer.data['index'],
                'description':serializer.data['description'],
                'project':serializer.data['project'],
                'responsible':serializer.data['responsible'],

             }
            return Response(responsing)
    

class Quality_issueAPIDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        
        quality_issue_list = Quality_issue.objects.get(id=pk)
        print(quality_issue_list)
        if quality_issue_list == "":
            sending = {
                    'error': 'Project does not found',
                    'error_code': 404,
                }
            return Response(sending ,status.HTTP_404_NOT_FOUND)
        else: return quality_issue_list
    
    def get(self, pk):
        if self.request.body == b'':
            qualilty_issue = self.get_object(pk)
            serializer = Quality_issueSerializer(qualilty_issue)
            print(qualilty_issue.name)
            print(serializer.data)
            responsing = {
                'name':serializer.data['name'],
                'description':serializer.data['description'],

             }
            return Response(responsing)

class Safety_issueAPIDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        
        Safety_issue_list = Safety_issue.objects.get(id=pk)
        print(Safety_issue_list)
        if Safety_issue_list == "":
            sending = {
                    'error': 'Project does not found',
                    'error_code': 404,
                }
            return Response(sending ,status.HTTP_404_NOT_FOUND)
        else: return Safety_issue_list
    
    def get(self, pk):
        if self.request.body == b'':
            safety_issue = self.get_object(pk)
            serializer = Safety_issueSerializer(safety_issue)
            print(safety_issue.name)
            print(serializer.data)
            responsing = {
                'name':serializer.data['name'],
                'description':serializer.data['description'],

             }
            return Response(responsing)

class Report_SafetyAPIDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        
        Report_Safety_list = Report_Safety.objects.get(id=pk)
        print(Report_Safety_list)
        if Report_Safety_list == "":
            sending = {
                    'error': 'Project does not found',
                    'error_code': 404,
                }
            return Response(sending ,status.HTTP_404_NOT_FOUND)
        else: return Report_Safety_list
    
    def get(self, pk):
        if self.request.body == b'':
            Report_Safety = self.get_object(pk)
            serializer = Report_SafetySerializer(Report_Safety)
            print(Report_Safety.name)
            print(serializer.data)
            responsing = {
                'photo':serializer.data['photo'],
                'name':serializer.data['name'],
                'author':serializer.data['author'],
                'responsible':serializer.data['responsible'],
                'room':serializer.data['room'],
                'created':serializer.data['created'],
                'updated':serializer.data['updated'],
                'is_active':serializer.data['is_active'],
                'status':serializer.data['status'],

             }
            return Response(responsing)

        fields = ['photo', 'name', 'author', 'responsible',
                  'room', 'created', 'updated', 'is_active', 'status']

class Report_QualityAPIDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        
        Report_Quality_list = Report_Quality.objects.get(id=pk)
        print(Report_Quality_list)
        if Report_Quality_list == "":
            sending = {
                    'error': 'Project does not found',
                    'error_code': 404,
                }
            return Response(sending ,status.HTTP_404_NOT_FOUND)
        else: return Report_Quality_list
    
    def get(self, pk):
        if self.request.body == b'':
            Report_Quality = self.get_object(pk)
            serializer = Report_QualitySerializer(Report_Quality)
            print(Report_Quality.name)
            print(serializer.data)
            responsing = {
                'photo':serializer.data['photo'],
                'name':serializer.data['name'],
                'author':serializer.data['author'],
                'responsible':serializer.data['responsible'],
                'room':serializer.data['room'],
                'created':serializer.data['created'],
                'updated':serializer.data['updated'],
                'is_active':serializer.data['is_active'],
                'status':serializer.data['status'],

             }
            return Response(responsing)

        fields = ['photo', 'name', 'author', 'responsible',
                  'room', 'created', 'updated', 'is_active', 'status']