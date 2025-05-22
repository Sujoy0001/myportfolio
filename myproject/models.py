from django.db import models
from myskills.models import Skill

class Project(models.Model):
    PROJECT_TYPES = [
        ('personal', 'Personal Project'),
        ('client', 'Client Work'),
        ('hackathon', 'Hackathon'),
        ('group', 'Group Project'),
    ]

    title = models.CharField(max_length=200)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    preview_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    project_date = models.DateField()
    skills_used = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.title
