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
