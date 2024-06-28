from django.urls import path
from .views import index, welcome, create_project, edit_project, edit_risk, new_risk, risklog, access_denied

urlpatterns = [
    path('', index, name='home'),
    path('welcome/', welcome, name='welcome'),
    path('project/new/', create_project, name='create_project'),
    path('project/<int:project_id>', edit_project, name='project'),
    path('project/risk/new', new_risk, name='new_risk'),
    path('project/risk/<int:risk_id>', edit_risk, name='risk'),
    path('project/risks/<int:project_id>', risklog, name='risks'),
    path('access-denied/', access_denied, name='access_denied'),
]

