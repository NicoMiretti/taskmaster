from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Board, BoardList
from .forms import BoardForm, BoardListForm
from apps.workspaces.models import Workspace


class BoardDetailView(LoginRequiredMixin, DetailView):
    model = Board
    template_name = 'boards/board_detail.html'
    context_object_name = 'board'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = self.object.lists.filter(is_archived=False).prefetch_related('tasks')
        return context


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'boards/board_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.workspace = get_object_or_404(Workspace, slug=self.kwargs['workspace_slug'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.workspace = self.workspace
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        
        # Create default lists
        default_lists = ['Por Hacer', 'En Progreso', 'Completado']
        for idx, list_name in enumerate(default_lists):
            BoardList.objects.create(
                board=self.object,
                name=list_name,
                position=idx
            )
        
        return response
    
    def get_success_url(self):
        return reverse_lazy('boards:board_detail', kwargs={'pk': self.object.pk})


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'boards/board_form.html'
    
    def get_success_url(self):
        return reverse_lazy('boards:board_detail', kwargs={'pk': self.object.pk})


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    template_name = 'boards/board_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('workspaces:workspace_detail', kwargs={'slug': self.object.workspace.slug})


class BoardListCreateView(LoginRequiredMixin, CreateView):
    model = BoardList
    form_class = BoardListForm
    template_name = 'boards/list_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.board = get_object_or_404(Board, pk=self.kwargs['board_pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.board = self.board
        max_position = BoardList.objects.filter(board=self.board).count()
        form.instance.position = max_position
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('boards:board_detail', kwargs={'pk': self.board.pk})

