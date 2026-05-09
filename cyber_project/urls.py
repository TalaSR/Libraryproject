from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='cyber_dashboard'),
    path('threats/', views.threat_list, name='threat_list'),
    path('tips/', views.security_tips, name='security_tips'),
    path('about/', views.about_project, name='about_project'),
    path('analytics/', views.cyber_analytics, name='cyber_analytics'),
]