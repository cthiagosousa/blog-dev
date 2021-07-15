from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.title
    
    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y %H:%M Hrs')
