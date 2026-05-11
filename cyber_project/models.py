from django.db import models

class ThreatCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SecurityReference(models.Model):
    source_name = models.CharField(max_length=100) 
    link = models.URLField()
    def __str__(self):
        return self.source_name

class CyberThreat(models.Model):
    RISK_LEVELS = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    name = models.CharField(max_length=100)
    description = models.TextField()
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    prevention_tips = models.TextField()
    category = models.ForeignKey(ThreatCategory, on_delete=models.CASCADE, null=True, blank=True)
    references = models.ManyToManyField(SecurityReference, blank=True)
    threat_image = models.ImageField(upload_to='threat_pics/', null=True, blank=True)

    def __str__(self):
        return self.name