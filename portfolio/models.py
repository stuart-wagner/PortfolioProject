from django.db import models
from django.utils.text import slugify

class SkillType(models.Model):
    """Category for grouping skills (e.g., Languages, Frameworks, AI Tools)"""
    ICON_CHOICES = [
        ('fas fa-code', 'Code'),
        ('fas fa-brain', 'Brain'),
        ('fas fa-cube', 'Cube'),
        ('fas fa-star', 'Star'),
        ('fas fa-database', 'Database'),
        ('fas fa-flask', 'Flask'),
        ('fas fa-cog', 'Cog'),
        ('fas fa-wrench', 'Wrench'),
        ('fas fa-tools', 'Tools'),
        ('fas fa-chart-line', 'Chart Line'),
        ('fas fa-rocket', 'Rocket'),
        ('fas fa-lightbulb', 'Lightbulb'),
        ('fas fa-laptop', 'Laptop'),
        ('fas fa-terminal', 'Terminal'),
        ('fas fa-book', 'Book'),
        ('fas fa-graduation-cap', 'Graduation Cap'),
    ]
    
    COLOR_CHOICES = [
        ('info', 'Blue (Info)'),
        ('warning', 'Yellow (Warning)'),
        ('success', 'Green (Success)'),
        ('danger', 'Red (Danger)'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('dark', 'Dark'),
        ('light', 'Light'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='info')
    order = models.PositiveIntegerField(default=0, help_text="Display order on skills page")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']


class Skill(models.Model):
    """Individual skill that belongs to a skill type"""
    name = models.CharField(max_length=200)
    skill_type = models.ForeignKey(SkillType, on_delete=models.CASCADE, related_name='skills')
    order = models.PositiveIntegerField(default=0, help_text="Display order within the skill type")
    
    def __str__(self):
        return f"{self.name} ({self.skill_type.name})"
    
    class Meta:
        ordering = ['skill_type', 'order', 'name']
        unique_together = ('name', 'skill_type')


class Portrait(models.Model):
    """Portrait photo displayed on the home page"""
    image = models.ImageField(upload_to='portraits/', help_text="PNG image with transparent background recommended")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, help_text="Set to True to display this portrait. Only one should be active.")

    def save(self, *args, **kwargs):
        if self.is_active:
            # Set all other portraits to inactive
            Portrait.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Portrait uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-uploaded_at']


class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500, help_text="One sentence summary")
    business_problem = models.TextField()
    tools_used = models.CharField(max_length=500, help_text="Comma-separated list")
    key_features = models.TextField()
    your_role = models.TextField()
    biggest_challenge = models.TextField()
    what_learned = models.TextField()
    screenshot = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order on projects page")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']


class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, help_text="Set to True to display this resume. Only one should be active.")

    def save(self, *args, **kwargs):
        if self.is_active:
            # Set all other resumes to inactive
            Resume.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Resume uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-uploaded_at']
