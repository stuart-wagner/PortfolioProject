from django.contrib import admin
from .models import Project, Resume, SkillType, Skill, Portrait

@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'icon', 'order')
    list_editable = ('order',)
    fields = ('name', 'icon', 'color', 'order')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'order')
    list_filter = ('skill_type',)
    list_editable = ('order',)
    search_fields = ('name', 'skill_type__name')
    fieldsets = (
        ('Skill Info', {'fields': ('name', 'skill_type', 'order')}),
    )


@admin.register(Portrait)
class PortraitAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uploaded_at', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('uploaded_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'summary', 'slug', 'order')}),
        ('Details', {'fields': ('business_problem', 'tools_used', 'key_features', 'your_role', 'biggest_challenge', 'what_learned')}),
        ('Media & Link', {'fields': ('screenshot', 'link')}),
    )

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uploaded_at', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('uploaded_at',)
