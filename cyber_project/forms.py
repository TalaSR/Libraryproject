from django import forms
from .models import CyberThreat, SecurityReference

class CyberThreatForm(forms.ModelForm):
    class Meta:
        model = CyberThreat
        fields = ['name', 'description', 'risk_level', 'prevention_tips', 'category', 'references', 'threat_image']
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'prevention_tips': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'risk_level': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'references': forms.CheckboxSelectMultiple(),
        }