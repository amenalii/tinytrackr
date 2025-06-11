from django.contrib import admin
from .models import Child, Activity, Journal

# Register your models here.
admin.site.register(Child)
admin.site.register(Activity)
admin.site.register(Journal)