from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Child, Activity
from .forms import ActivityForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    children = Child.objects.filter(user=request.user)
    return render(request, 'main_app/dashboard.html', {'children': children})

def child_detail(request, child_id):
    child = Child.objects.get(id=child_id, user=request.user)
    activities = Activity.objects.filter(child=child).order_by('-date', '-time')  # Now Groups activities by date and time with most recent at the top
    activity_form = ActivityForm()
    return render(request, 'main_app/child_detail.html', {'child': child, 'activities': activities, 'activity_form': activity_form})

class ChildCreate(CreateView):
    model = Child
    fields = ['name', 'date_of_birth', 'gender', 'notes'] 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ChildUpdate(UpdateView):
    model = Child
    fields = ['name', 'date_of_birth', 'gender', 'notes'] 

class ChildDelete(DeleteView):
    model = Child
    success_url = '/dashboard/'  

def add_activity(request, child_id):
    form = ActivityForm(request.POST)
    if form.is_valid():
        activity = form.save(commit=False)
        activity.child_id = child_id
        activity.save()
        return redirect('child-detail', child_id=child_id)
    
class ActivityUpdate(UpdateView):
    model = Activity
    form_class = ActivityForm  #Attribute allows us to use custom form
    template_name = 'main_app/edit_activity_form.html' # Needed a template for update view as it does not use the default form template

    # To retrieve the child's data get_context_data method is used to pass additional context to the template.
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) # Calling the parent class's method to get the default context
        context['child'] = self.object.child # This adds the child object to the context so it can be accessed in the template
        return context 

    def get_success_url(self):
        return self.object.child.get_absolute_url()
    
class ActivityDelete(DeleteView):
    model = Activity

    def get_success_url(self):
        return self.object.child.get_absolute_url()


################################### RESOURCES ########################################
# https://www.w3schools.com/django/django_queryset_orderby.php
# https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-editing/
# https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-display/