from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_students, name='get_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/update/<int:pk>/', views.update_student, name='update_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
]