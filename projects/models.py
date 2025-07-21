from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completion_date = models.DateField()
    location = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project.title} - {self.caption if self.caption else 'Image'}"
