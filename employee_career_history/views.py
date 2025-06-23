from django.shortcuts import render, redirect, get_object_or_404
from employee_profile.models import User
from .models import CareerHistory
from django.urls import reverse
from django.views.decorators.http import require_POST


def career_history_index(request):
    user = User.objects.last()

    if not user:
        return render(request, "employee_career_history/index.html", {'user': None})

    if request.method == "POST":
        career_id = request.POST.get("career_id")
        file = request.FILES.get('file')

        if career_id:
            career = CareerHistory.objects.get(id=career_id)
        else:
            career = CareerHistory(user=user)
            
        career.job_position = request.POST.get("job_position")
        career.job_level = request.POST.get("job_level")
        career.employee_status = request.POST.get("employee_status")
        career.start_date = request.POST.get("start_date")
        career.end_date = request.POST.get("end_date")

        if file:
            career.file = file

        career.save()
        return redirect("career_list")

    careers = user.career_histories.all()
    return render(request, "employee_career_history/index.html", {
        'careers': careers,
        'user': user
    })

def delete_career_history(request, id):
    career = get_object_or_404(CareerHistory, id=id)
    career.delete()
    return redirect("career_list")
