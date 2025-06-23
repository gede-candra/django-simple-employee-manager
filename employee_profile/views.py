from django.shortcuts import redirect, render
from .models import User

def profile(request):
    if request.method == "POST":
        User.objects.create(
            id_employee=request.POST.get("id_employee"),
            name=request.POST.get("name"),
            department=request.POST.get("department"),
            job_position=request.POST.get("job_position"),
            join_date=request.POST.get("join_date"),
            day_payment=request.POST.get("day_payment"),
            job_level=request.POST.get("job_level"),
            employment_status=request.POST.get("employment_status"),
            end_date=request.POST.get("end_date") or None
        )
        return redirect('employee_profile')

    employee = User.objects.last()
    return render(request, 'employee_profile/index.html', {'employee': employee})