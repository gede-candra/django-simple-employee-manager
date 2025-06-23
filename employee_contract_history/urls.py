from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('save/', views.save_contract, name='save_contract'),
    path('delete/<int:contract_number>/', views.delete_contract, name='delete_contract'),
]