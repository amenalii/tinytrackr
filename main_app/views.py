from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Child, Activity, Journal
from .forms import ActivityForm, JournalForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView


class Home(LoginView):
    template_name = 'home.html'

class SignIn(LoginView):
    template_name = 'signin.html'

@login_required
def dashboard(request):
    children = Child.objects.filter(user=request.user)
    journal_entries = Journal.objects.filter(user=request.user).order_by('-date')
    return render(request, 'main_app/dashboard.html', {
        'children': children,
        'journal_entries': journal_entries
    })

@login_required
def child_detail(request, child_id):
    child = Child.objects.get(id=child_id, user=request.user)
    activities = Activity.objects.filter(child=child).order_by('-date', '-time')  # Now Groups activities by date and time with most recent at the top
    activity_form = ActivityForm()
    return render(request, 'main_app/child_detail.html', {'child': child, 'activities': activities, 'activity_form': activity_form})

class ChildCreate(LoginRequiredMixin, CreateView):
    model = Child
    fields = ['name', 'date_of_birth', 'gender', 'notes'] 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ChildUpdate(LoginRequiredMixin, UpdateView):
    model = Child
    fields = ['name', 'date_of_birth', 'gender', 'notes'] 

class ChildDelete(LoginRequiredMixin, DeleteView):
    model = Child
    success_url = '/dashboard/'  

@login_required
def add_activity(request, child_id):
    form = ActivityForm(request.POST)
    if form.is_valid():
        activity = form.save(commit=False)
        activity.child_id = child_id
        activity.save()
        return redirect('child-detail', child_id=child_id)
    
class ActivityUpdate(LoginRequiredMixin, UpdateView):
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
    
class ActivityDelete(LoginRequiredMixin, DeleteView):
    model = Activity

    def get_success_url(self):
        return self.object.child.get_absolute_url()


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def journal_detail(request, journal_id):
    journal = Journal.objects.get(id=journal_id, user=request.user)
    return render(request, 'journal/journal_detail.html', {'journal': journal})


class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal/journal_form.html'  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal/journal_form.html'  

    def get_success_url(self):
        return self.object.get_absolute_url()  


class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    
    def get_success_url(self):
        return '/dashboard/'  

class JournalListView(LoginRequiredMixin, ListView):
    model = Journal
    template_name = 'journal/journal_list.html'  
    context_object_name = 'journals' 
    
    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user).order_by('-date')  





################################### RESOURCES ########################################
# https://www.w3schools.com/django/django_queryset_orderby.php
# https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-editing/
# https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-display/