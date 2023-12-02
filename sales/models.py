from django.db import models


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="No Position")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    age = models.IntegerField(default=0)
    position = models.CharField(max_length=100, default="No Position")
    availability = models.BooleanField(default=False)
    
    def __str__(self):
        return self.position