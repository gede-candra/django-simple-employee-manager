from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # atau sesuaikan path template-nya
