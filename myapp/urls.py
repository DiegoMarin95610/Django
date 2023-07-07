from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('projects/', views.Projects, name='projects'),
    path('tasks/', views.Tasks, name='tasks'),
    path('create_new_task/', views.Create_task, name='new_task'),
    path('create_new_project/', views.Create_project, name='new_project')
    
    
]
