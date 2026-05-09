from django.db import models

class CyberThreat(models.Model):
    RISK_LEVELS = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    prevention_tips = models.TextField()

    def __str__(self):
        return self.name