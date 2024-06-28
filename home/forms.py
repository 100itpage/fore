from django import forms
from .models import Project, Risk

class RiskForm(forms.ModelForm):
  class Meta:
    model = Risk
    fields = ['title', 'category', 'likelihood', 'description', 'impact', 'status', 'approach']

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'description', 'technology', 'budget', 'start_date', 'end_date', 'sdlc']  # Adjust fields as needed