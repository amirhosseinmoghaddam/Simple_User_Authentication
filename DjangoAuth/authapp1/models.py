from django.db import models

class UserData(models.Model):
    username = models.CharField(max_length=1000)
    cars = models.CharField(max_length=256)

    def __str__(self):
        return self.cars