from django.db import models
from employee_profile.models import User
import uuid

class CareerHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="career_histories")
    job_position = models.CharField(max_length=100)
    job_level = models.CharField(max_length=50)
    employee_status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    file = models.FileField(upload_to='career_history_documents/', null=True, blank=True)

    def __str__(self):
        return f"{self.job_position} - {self.user.name}"
