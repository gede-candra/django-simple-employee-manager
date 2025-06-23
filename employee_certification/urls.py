from django.urls import path
from . import views

urlpatterns = [
    path('', views.certification_list, name='certification_list'),
    path('delete/<int:id>/', views.delete_certification, name='delete_certification'),
]
