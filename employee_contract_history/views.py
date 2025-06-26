import pprint
from django.shortcuts import render, get_object_or_404, redirect
from .models import ContractHistory
from employee_profile.models import User
from django.views.decorators.http import require_http_methods

def contract_list(request):
    user = User.objects.last()

    if not user:
        return render(request, "employee_contract_history/index.html", {'user': None})

    if request.method == "POST":
        contract_id = request.POST.get("contract_id")
        file = request.FILES.get('file')

        if contract_id:
            contract = ContractHistory.objects.get(id=contract_id)
        else:
            contract = ContractHistory(user=user)
            
        contract.contract_number = request.POST.get('contract_number')
        contract.contract_name = request.POST.get('contract_name')
        contract.start_date = request.POST.get('start_date')
        contract.end_date = request.POST.get('end_date')

        if file:
            contract.file = file

        contract.save()
        return redirect("contract_list")

    contracts = user.contract_histories.all()
    return render(request, "employee_contract_history/index.html", {
        'contracts': contracts,
        'user': user
    })

def delete_contract(request, id):
    contract = get_object_or_404(ContractHistory, id=id)
    contract.delete()
    return redirect('contract_list')
