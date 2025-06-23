from django.db import models
from employee_profile.models import User

class Certification(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certifications")
    certification_name = models.CharField(max_length=100)
    certification_number = models.CharField(max_length=100)
    date_issued = models.DateField()
    validity_period = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='certification_documents/', null=True, blank=True)

    def __str__(self):
        return f"{self.certification_name} ({self.certification_number})"
