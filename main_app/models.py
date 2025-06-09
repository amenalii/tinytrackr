from django.db import models
from django.contrib.auth.models import User
from datetime import date # Imprt date for comparison to ensure the date of birth is not in the future
from django.urls import reverse

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NB', 'Non-binary'),
    ('O', 'Other'),
    ('P', 'Prefer not to say'),
]

class Child(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Adding functio to determine child's age
    # Migration not needed since database schema is not being changed. 
    @property # Property decorator allows us to access this method like an attribute
    def age(self):
        today = date.today() 
        dob = self.date_of_birth
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('child-detail', kwargs={'child_id': self.id})


class Activity(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    activity_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.activity_type} - {self.child.name} on {self.date}"



##################################################################################################################
## RESORUCES
# https://medium.com/@katheller/how-to-convert-birthdate-into-an-integer-and-count-age-in-django-c6fd403baa84