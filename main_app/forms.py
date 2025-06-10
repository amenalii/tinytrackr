from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'time', 'activity_type', 'location', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'Select a date','type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'activity_type': forms.TextInput(attrs={'placeholder': 'Enter activity type'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location (optional)'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description (optional)', 'rows': 2}),
        }