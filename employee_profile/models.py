from django.db import models

class User(models.Model):
    id_employee = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    join_date = models.DateField()
    day_payment = models.DecimalField(max_digits=10, decimal_places=2)
    job_level = models.CharField(max_length=50)
    employment_status = models.CharField(max_length=50)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id_employee} - {self.job_position}'