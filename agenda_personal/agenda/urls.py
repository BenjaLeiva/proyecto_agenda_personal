from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('signup/', views.signup, name='signup'),
]
