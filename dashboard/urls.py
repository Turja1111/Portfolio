from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Projects
    path('projects/', views.projects_list, name='projects'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # Skills
    path('skills/', views.skills_list, name='skills'),
    path('skills/create/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),

    # Messages
    path('messages/', views.messages_list, name='messages'),
    path('messages/<int:pk>/read/', views.message_mark_read, name='message_read'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
]
