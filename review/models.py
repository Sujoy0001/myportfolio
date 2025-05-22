from django.db import models

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    client_image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    is_active = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return f"{self.client_name} - {self.get_rating_display()}"