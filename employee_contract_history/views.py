from django.shortcuts import render, get_object_or_404, redirect
from .models import ContractHistory
from employee_profile.models import User
from django.views.decorators.http import require_http_methods


def contract_list(request):
    user = User.objects.last()
    contracts = ContractHistory.objects.filter(user=user)
    return render(request, 'employee_contract_history/index.html', {
        'user': user,
        'contracts': contracts
    })


@require_http_methods(["POST"])
def save_contract(request):
    user = User.objects.last()
    contract_number = request.POST.get('contract_number')

    contract = ContractHistory.objects.filter(contract_number=contract_number).first()
    if contract:
        contract.contract_name = request.POST.get('contract_name')
        contract.start_date = request.POST.get('start_date')
        contract.end_date = request.POST.get('end_date')
        if request.FILES.get('file'):
            contract.file = request.FILES.get('file')
        contract.save()
    else:
        ContractHistory.objects.create(
            user=user,
            contract_number=contract_number,
            contract_name=request.POST.get('contract_name'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            file=request.FILES.get('file') if request.FILES.get('file') else None
        )

    return redirect('contract_list')


def delete_contract(request, contract_number):
    contract = get_object_or_404(ContractHistory, contract_number=contract_number)
    contract.delete()
    return redirect('contract_list')
