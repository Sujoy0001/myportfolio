from django.db import models

class Skill(models.Model):
    SKILLS_CATEGORY = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps & Deployment'),
        ('design', 'Design'),
        ('other', 'Tools & Other'),
    )
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=SKILLS_CATEGORY, default='other')
    proficiency = models.PositiveIntegerField(default=80, help_text="Skill level (0-100)")
    
    order = models.PositiveIntegerField(default=100)  

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return self.name