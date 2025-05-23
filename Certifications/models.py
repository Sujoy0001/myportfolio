from django.db import models

class Certificate(models.Model):
    CATEGORY_CHOICES = [
        ('lerning', 'Learning'),
        ('hackathon', 'Hackathon'),
        ('competition', 'Competition'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/')
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    skills = models.TextField(help_text="Comma separated list of skills", blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.issuing_organization}"
    
    def get_skills_list(self):
        return [skill.strip() for skill in self.skills.split(',')] if self.skills else []