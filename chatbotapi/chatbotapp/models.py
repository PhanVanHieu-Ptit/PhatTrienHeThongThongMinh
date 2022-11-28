from django.db import models

# Create your models here.
class ChatResponse(models.Model):
    tag = models.CharField(max_length=100)
    response = models.CharField(max_length=100)

