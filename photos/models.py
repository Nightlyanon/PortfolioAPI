from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100, blank=True)
    art = models.ImageField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

