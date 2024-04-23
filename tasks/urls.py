from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('completed/<int:pk>/', views.mark_completed, name='mark_completed'),
    path('notcompleted/<int:pk>/', views.mark_not_completed, name='mark_not_completed'),
]
