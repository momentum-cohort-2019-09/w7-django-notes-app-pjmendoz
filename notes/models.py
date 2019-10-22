from django.db import models
from django.utils import timezone
# Create your models here.

class Note(models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Any instructions people need to use this note app.", 
        blank=True, 
        null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)    
    
    def __str(self):
        return self.title