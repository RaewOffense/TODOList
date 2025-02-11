from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_task,name = 'readTask'),
    path('addtask/', views.add_task, name = 'addTask'),
    path('updateTask/<int:task_id>/',views.update_task,name = 'updateTask'),
    path('deleteTask/<int:task_id>/',views.delete_task, name = 'deleteTask')
   
]