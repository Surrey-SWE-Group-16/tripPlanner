from django.db import models
from django.contrib.auth.models import User


# Create your models here
# MapModel
class MapModel(models.Model):
    title = models.CharField(max_length=50)
    orig_loc = models.CharField(max_length=50)
    dest_loc = models.CharField(max_length=50)
    waypoints = models.TextField()
    check_item = models.TextField()
    journal = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # whenever a user is deleted, deletes everything related to that user

    def __str__(self):
        return self.location_points


