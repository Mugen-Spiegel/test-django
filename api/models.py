from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    code_block = models.CharField(max_length=255)
    active = models.CharField(max_length=30)
