from django.db import models

# Create your models here.


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=60)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.timestamp} {self.level} {self.message}"
    