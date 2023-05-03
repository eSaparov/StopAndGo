"""
URL configuration for StopAndGo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from backend.views import *
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('api/project', ProjectAPIListView.as_view(), name='api_projects_list'),
    path('api/project/<int:pk>', ProjectAPIDetailView.as_view(), name='api_project_detail'),
    path('api/room', RoomAPIListView.as_view(), name='api_rooms_list'),
    path('api/room/<int:pk>', RoomAPIDetailView.as_view(), name='api_room_detail'),
    path('api/quality_issue', Quality_issueAPIListView.as_view(), name='api_quality_issues_list'),
    path('api/quality_issue/<int:pk>', Quality_issueAPIDetailView.as_view(), name='api_quality_issue_detail'),
    path('api/safety_issue', Safety_issueAPIListView.as_view(), name='api_safety_issues_list'),
    path('api/safety_issue/<int:pk>', Safety_issueAPIDetailView.as_view(), name='api_safety_issue_detail'),
    path('api/report_safety', Report_SafetyAPIListView.as_view(), name='api_report_safetys_list'),
    path('api/report_safety/<int:pk>', Report_SafetyAPIDetailView.as_view(), name='api_report_safety_detail'),
    path('api/report_quality', Report_QualityAPIListView.as_view(), name='api_report_qualitys_list'),
    path('api/report_quality/<int:pk>', Report_QualityAPIDetailView.as_view(), name='api_report_quality_detail'),
    path('openapi', get_schema_view(
            title="StopAndGo",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),

]
