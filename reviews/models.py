from django.db import models

class Review(models.Model):
    text = models.TextField()
    predicted_stars = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
