from django.db import models

# Create your models here.

class Note(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Any instructions people need to use this note app.", 
        blank=True, 
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str(self):
        return self.title