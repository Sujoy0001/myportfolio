from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.name
