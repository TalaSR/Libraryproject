from django.shortcuts import render, redirect
from django.db.models import Count, Q
from .models import CyberThreat, ThreatCategory
from .forms import CyberThreatForm

def dashboard(request):
    total_threats = CyberThreat.objects.count()
    return render(request, 'cyber_project/dashboard.html', {'total_threats': total_threats})

def threat_list(request):
    query = request.GET.get('q')
    if query:
        threats = CyberThreat.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        threats = CyberThreat.objects.all().prefetch_related('references')
    return render(request, 'cyber_project/threat_list.html', {'threats': threats})

def cyber_analytics(request):
    total = CyberThreat.objects.count()
    high_risk = CyberThreat.objects.filter(risk_level='High').count()
    stats_by_category = ThreatCategory.objects.annotate(threat_count=Count('cyberthreat'))
    context = {
        'total': total,
        'high_risk': high_risk,
        'stats_by_category': stats_by_category,
        'risk_percent': (high_risk / total * 100) if total > 0 else 0
    }
    return render(request, 'cyber_project/analytics.html', context)

def add_threat(request):
    if request.method == 'POST':
        form = CyberThreatForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('threat_list')
    else:
        form = CyberThreatForm()
    return render(request, 'cyber_project/add_threat.html', {'form': form})

def security_tips(request):
    return render(request, 'cyber_project/security_tips.html')