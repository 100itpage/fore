from django.contrib import admin
from .models import Project, Risk

# Register Project model with admin
admin.site.register(Project)

# Register Risk model with admin
@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
  # Customize the list display in the admin interface
  list_display = ('title', 'project', 'category', 'likelihood', 'created_at')

  # Add a filter by project in the admin interface
  list_filter = ('project',)