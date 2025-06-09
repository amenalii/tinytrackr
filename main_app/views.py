from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Child, Activity

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    children = Child.objects.filter(user=request.user)
    return render(request, 'main_app/dashboard.html', {'children': children})

def child_detail(request, child_id):
    child = Child.objects.get(id=child_id, user=request.user)
    activities = Activity.objects.filter(child=child).order_by('-date', '-time')  # Now Groups activities by date and time with most recent at the top
    return render(request, 'main_app/child_detail.html', {'child': child, 'activities': activities})

class ChildCreate(CreateView):
    model = Child
    fields = ['name', 'date_of_birth', 'gender', 'notes'] 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

################################### RESOURCES ########################################
# https://www.w3schools.com/django/django_queryset_orderby.php