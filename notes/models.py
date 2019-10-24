from django.db import models
from django.utils import timezone
# Create your models here.

class Note(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField(
        blank=True, 
        null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)    
    
    def __str(self):
        return self.title