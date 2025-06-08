from django.shortcuts import render
from .models import Child, Activity

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    children = Child.objects.filter(user=request.user)
    return render(request, 'main_app/dashboard.html', {'children': children})