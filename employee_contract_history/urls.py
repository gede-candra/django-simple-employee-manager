from django.urls import path
from . import views

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('delete/<int:id>/', views.delete_contract, name='delete_contract'),
]