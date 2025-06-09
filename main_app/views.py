from django.shortcuts import render
from .models import Child, Activity

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    children = Child.objects.filter(user=request.user)
    return render(request, 'main_app/dashboard.html', {'children': children})

def child_detail(request, child_id):
    child = Child.objects.get(id=child_id, user=request.user)
    activities = Activity.objects.filter(child=child)
    return render(request, 'main_app/child_detail.html', {'child': child, 'activities': activities})
