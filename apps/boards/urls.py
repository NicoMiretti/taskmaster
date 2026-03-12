from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('<int:pk>/', views.BoardDetailView.as_view(), name='board_detail'),
    path('create/<slug:workspace_slug>/', views.BoardCreateView.as_view(), name='board_create'),
    path('<int:pk>/edit/', views.BoardUpdateView.as_view(), name='board_edit'),
    path('<int:pk>/delete/', views.BoardDeleteView.as_view(), name='board_delete'),
    path('<int:board_pk>/list/create/', views.BoardListCreateView.as_view(), name='list_create'),
]
