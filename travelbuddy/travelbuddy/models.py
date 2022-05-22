from django.db import models
from django.contrib.auth.models import User


# Create your models here
# MapModel
class MapModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_points = models.TextField()

    def __str__(self):
        return self.location_points


# Checklist model
class ChecklistModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checklist = models.TextField()

    def __str__(self):
        return self.checklist


# Journal model
class JournalModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journal = models.TextField()

    def __str__(self):
        return self.journal
