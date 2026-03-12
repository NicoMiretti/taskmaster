from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create/<int:list_pk>/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/toggle-complete/', views.TaskToggleCompleteView.as_view(), name='task_toggle_complete'),
    path('<int:pk>/move/', views.TaskMoveView.as_view(), name='task_move'),
]
