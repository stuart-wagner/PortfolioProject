from django.contrib import admin
from .models import Project, Resume

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'summary', 'slug')}),
        ('Details', {'fields': ('business_problem', 'tools_used', 'key_features', 'your_role', 'biggest_challenge', 'what_learned')}),
        ('Media & Link', {'fields': ('screenshot', 'link')}),
    )

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uploaded_at', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('uploaded_at',)
