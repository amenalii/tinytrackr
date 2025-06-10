from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('children/<int:child_id>/', views.child_detail, name='child-detail'),
    path('children/create/', views.ChildCreate.as_view(), name='add-child'),
    path('children/<int:pk>/update/', views.ChildUpdate.as_view(), name='update-child'),
    path('children/<int:pk>/delete/', views.ChildDelete.as_view(), name='delete-child'),
    path('children/<int:child_id>/add-activity/', views.add_activity, name='add-activity'),
]