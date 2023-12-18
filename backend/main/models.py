from django.db import models

# Create your models here.
class RequestMech(models.Model):
    car_owner = models.CharField(max_length = 50)
    location = models.CharField(max_length=50)
    car_issue = models.TextField()
    priority = models.CharField(max_length=55)
    expected_time = models.IntegerField()
    expected_budget = models.IntegerField()
    mech = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.car_owner} at {self.location}'