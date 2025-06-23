from django.shortcuts import render, redirect, get_object_or_404
from .models import Certification
from employee_profile.models import User

def certification_list(request):
    user = User.objects.last()

    if not user:
        return render(request, "employee_certification/index.html", {'user': None})

    if request.method == "POST":
        cert_id = request.POST.get('cert_id')
        file = request.FILES.get('file')

        if cert_id:
            cert = Certification.objects.get(id=cert_id)
        else:
            cert = Certification(user=user)

        cert.certification_name = request.POST.get('certification_name')
        cert.certification_number = request.POST.get('certification_number')
        cert.date_issued = request.POST.get('date_issued')
        cert.validity_period = request.POST.get('validity_period')
        cert.description = request.POST.get('description')

        if file:
            cert.file = file

        cert.save()
        return redirect('certification_list')

    certifications = user.certifications.all()
    return render(request, "employee_certification/index.html", {
        'certifications': certifications,
        'user': user
    })

def delete_certification(request, id):
    cert = get_object_or_404(Certification, id=id)
    cert.delete()
    return redirect('certification_list')
