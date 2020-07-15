from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    done = models.BooleanField(default=False)