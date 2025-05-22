from django.db import models

class UserProfile(models.Model):
    userName = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    tagline = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    x = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    institution = models.TextField(blank=True, null=True)
    degree = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, default="Location")
    contact_email = models.EmailField()
    experience_year = models.IntegerField(default=0, help_text="Years of experience in the field")
    achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.userName
    
    
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    additional_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.question
