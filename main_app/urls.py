from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('children/<int:child_id>/', views.child_detail, name='child-detail'),
    path('children/create/', views.ChildCreate.as_view(), name='add-child'),
    path('children/<int:pk>/update/', views.ChildUpdate.as_view(), name='update-child'),
    path('children/<int:pk>/delete/', views.ChildDelete.as_view(), name='delete-child'),
    path('children/<int:child_id>/add-activity/', views.add_activity, name='add-activity'),
    path('children/<int:pk>/activity/update/', views.ActivityUpdate.as_view(), name='update-activity'),
    path('children/<int:pk>/activity/delete/', views.ActivityDelete.as_view(), name='delete-activity'),
    path('accounts/signup/', views.signup, name='signup'),
    path('journal/<int:journal_id>/', views.journal_detail, name='journal-detail'),
    path('journal/add/', views.JournalCreate.as_view(), name='add-journal'),
    path('journal/<int:pk>/update/', views.JournalUpdate.as_view(), name='update-journal'),
    path('journal/<int:pk>/delete/', views.JournalDelete.as_view(), name='delete-journal'),
    path('journal/', views.JournalListView.as_view(), name='journal-list'),
    path('signin/', views.SignIn.as_view(), name='signin'),

]