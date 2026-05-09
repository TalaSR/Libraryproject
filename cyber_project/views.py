from django.shortcuts import render
from .models import CyberThreat

def dashboard(request):
    total_threats = CyberThreat.objects.count()
    return render(request, 'cyber_project/dashboard.html', {'total_threats': total_threats})

def threat_list(request):
    threats = CyberThreat.objects.all()
    return render(request, 'cyber_project/threat_list.html', {'threats': threats})

def security_tips(request):
    return render(request, 'cyber_project/security_tips.html')

def about_project(request):
    return render(request, 'cyber_project/about.html')
def cyber_analytics(request):
    from .models import CyberThreat
    total = CyberThreat.objects.count()
    high_risk = CyberThreat.objects.filter(risk_level='High').count()
    
    context = {
        'total': total,
        'high_risk': high_risk,
    }
    return render(request, 'cyber_project/analytics.html', context)