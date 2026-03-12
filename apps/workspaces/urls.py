from django.urls import path
from . import views

app_name = 'workspaces'

urlpatterns = [
    path('', views.WorkspaceListView.as_view(), name='workspace_list'),
    path('create/', views.WorkspaceCreateView.as_view(), name='workspace_create'),
    path('<slug:slug>/', views.WorkspaceDetailView.as_view(), name='workspace_detail'),
    path('<slug:slug>/edit/', views.WorkspaceUpdateView.as_view(), name='workspace_edit'),
    path('<slug:slug>/delete/', views.WorkspaceDeleteView.as_view(), name='workspace_delete'),
]
