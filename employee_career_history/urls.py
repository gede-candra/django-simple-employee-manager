from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_history_index, name='career_list'),
    path('delete/<int:id>/', views.delete_career_history, name='delete_career_history'),
]
