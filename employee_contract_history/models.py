from django.db import models
from employee_profile.models import User

class ContractHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contract_histories")
    contract_number = models.CharField(max_length=100)
    contract_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    file = models.FileField(upload_to='contract_history_documents/', null=True, blank=True)

    def __str__(self):
        return f"{self.contract_number} - {self.user.name}"