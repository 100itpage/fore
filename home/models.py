from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link project to a user
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-fill creation date
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    technology = models.CharField(max_length=255, blank=True)  # Optional project technology
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional project budget

    SDLC_CHOICES = (
        ('AGILE', 'Agile'),
        ('WATERFALL', 'Waterfall'),
        ('OTHER', 'Other'),
    )
    sdlc = models.CharField(max_length=50, choices=SDLC_CHOICES, default='AGILE')

    def __str__(self):
        return f"{self.user.username} - {self.name}"

from django.db import models

class Risk(models.Model):
    CATEGORY_CHOICES = (
        ('MANAGEMENT', 'Management'),
        ('TECHNICAL', 'Technical'),
        ('FINANCIAL', 'Financial'),
        ('EXTERNAL', 'External'),
    )
    LIKELIHOOD_CHOICES = (
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('OPEN', 'Open'),
        ('MONITORING', 'Monitoring'),
        ('MITIGATING', 'Mitigating'),
        ('CONTINGENCY', 'Contingency'),
        ('CLOSED', 'Closed'),
        ('REOPENED', 'Reopened'),
    )
    APPROACH_CHOICES = (
        ('REDUCE', 'Reduce'),
        ('ACCEPT', 'Accept'),
        ('AVOID', 'Avoid'),
        ('SHARE', 'Share'),
        ('TRANSFER', 'Transfer'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Link risk to a project
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    likelihood = models.CharField(max_length=10, choices=LIKELIHOOD_CHOICES)
    impact = models.IntegerField()  # Impact of the risk (integer value)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-fill creation date
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='NEW')
    approach = models.CharField(max_length=50, choices=APPROACH_CHOICES, blank=True)  # Approach can be blank

    def __str__(self):
        return f"Risk: {self.title} - Project: {self.project.name}"


