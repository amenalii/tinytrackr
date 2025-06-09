from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('children/<int:child_id>/', views.child_detail, name='child-detail'),
]