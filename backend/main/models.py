from django.db import models
from accounts.models import CustomUser

# Create your models here.
class RequestMech(models.Model):
    car_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='car_owner')
    location = models.CharField(max_length=50)
    car_issue = models.TextField()
    priority = models.CharField(max_length=55)
    expected_time = models.IntegerField()
    expected_budget = models.IntegerField()
    mech = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mechanic')
    created_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.car_owner} at {self.location}'
