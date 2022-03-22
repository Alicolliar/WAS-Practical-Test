from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=128)
    startDate = models.DateField()
    description = models.CharField(max_length=384)

    def __str__(self):
        return self.title
