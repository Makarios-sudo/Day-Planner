from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class DailyPlan(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE,)
    task = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    task_complete = models.BooleanField(blank=True, null=True)
    deadline_day = models.DateField(auto_now_add=False, blank=False, null=False)
    deadline_time = models.TimeField(auto_now_add=False, blank=True, null=True)
    

    def __str__(self):
        return self.task



