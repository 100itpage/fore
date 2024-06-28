from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Risk  # Import the Project model
from .forms import ProjectForm, RiskForm


# Create your views here.

def index(request):
  context = {}
  return render(request, 'index.html', context)


@login_required
def welcome(request):
  # Check if user has any projects
  projects = Project.objects.filter(user=request.user)
  has_project = projects.exists()  # Check if any projects exist for the user
  context = {
    'projects': projects,
    'has_project': has_project,
  }
  return render(request, 'welcome.html', context)


@login_required
def create_project(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      project = form.save(commit=False)
      project.user = request.user
      project.save()
      return redirect('welcome') 
  else:
    form = ProjectForm()
  return render(request, 'project_form.html', {'form': form})

@login_required
def edit_project(request, project_id):
  project = get_object_or_404(Project, pk=project_id, user=request.user)
  if project.user != request.user:
    return redirect('access_denied')
  if request.method == 'POST':
    form = ProjectForm(request.POST, instance=project) 
    if form.is_valid():
      form.save()
      return redirect('welcome') 
  else:
    form = ProjectForm(instance=project) 
  context = {'form': form, 'project': project}
  return render(request, 'project.html', context)


@login_required
def risklog(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  if project.user != request.user:
    return redirect('access_denied')
  risks = Risk.objects.filter(project=project)
  context = {
    'risks': risks,
    'project': project,
  }
  return render(request, 'risklog.html', context)


@login_required
def new_risk(request):
  project = get_object_or_404(Project, user=request.user)
  if request.method == 'POST':
    form = RiskForm(request.POST)
    if form.is_valid():
      risk = form.save(commit=False) 
      risk.project = project 
      risk.save()
      return redirect('welcome')  
  else:
    form = RiskForm()
  context = {
    'form': form,
    'project': project,
  }
  return render(request, 'new_risk.html', context)


@login_required
def edit_risk(request, risk_id):
  risk = get_object_or_404(Risk, pk=risk_id)
  if risk.project.user != request.user:
    return redirect('access_denied')
  if request.method == 'POST':
    form = RiskForm(request.POST, instance=risk) 
    if form.is_valid():
      form.save()
      return redirect('welcome')  
  else:
    form = RiskForm(instance=risk)
  context = {'form': form, 'risk': risk}
  return render(request, 'risk.html', context)


def access_denied(request):
  return render(request, 'access_denied.html')