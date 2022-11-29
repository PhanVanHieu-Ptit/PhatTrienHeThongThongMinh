from django.db import models

# Create your models here.
class ChatResponse(models.Model):
    id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=100)
    response = models.CharField(max_length=100)

