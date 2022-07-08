from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f'{self.name} - {self.description[:20]}'
