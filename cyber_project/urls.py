from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('dashboard/', views.dashboard, name='cyber_dashboard'),
    path('threats/', views.threat_list, name='threat_list'),
    path('tips/', views.security_tips, name='security_tips'),
    path('analytics/', views.cyber_analytics, name='cyber_analytics'),
    path('add-threat/', views.add_threat, name='add_threat'),
    path('admin/', admin.site.urls), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)