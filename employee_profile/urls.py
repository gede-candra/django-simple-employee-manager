from django.urls import path
from .views import profile

urlpatterns = [
    path('', profile, name='employee_profile'),
]
