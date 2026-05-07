from django.db import models
from django.utils.text import slugify

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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

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
