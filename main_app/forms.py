from django import forms
from .models import Activity, Journal


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


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'entry']
        widgets = {
            'title': forms.TextInput,
            'entry': forms.Textarea(attrs={'rows': 10}),
        }