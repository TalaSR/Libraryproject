from django.contrib import admin
from .models import CyberThreat, ThreatCategory, SecurityReference

admin.site.register(ThreatCategory)
admin.site.register(CyberThreat)
admin.site.register(SecurityReference)