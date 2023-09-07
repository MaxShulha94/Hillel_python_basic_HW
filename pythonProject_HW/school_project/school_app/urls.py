from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('api/schools/', views.SchoolListCreateView.as_view(), name='school-list'),
    path('api/schools/<int:pk>/', views.SchoolDetailView.as_view(), name='school-detail'),
    path('api/students/', views.StudentListCreateView.as_view(), name='student-list'),
    path('api/students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),]