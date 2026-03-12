from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Workspace, WorkspaceMember
from .forms import WorkspaceForm


class WorkspaceListView(LoginRequiredMixin, ListView):
    model = Workspace
    template_name = 'workspaces/workspace_list.html'
    context_object_name = 'workspaces'
    
    def get_queryset(self):
        return Workspace.objects.filter(members=self.request.user, is_active=True)


class WorkspaceDetailView(LoginRequiredMixin, DetailView):
    model = Workspace
    template_name = 'workspaces/workspace_detail.html'
    context_object_name = 'workspace'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = self.object.boards.filter(is_archived=False)
        return context


class WorkspaceCreateView(LoginRequiredMixin, CreateView):
    model = Workspace
    form_class = WorkspaceForm
    template_name = 'workspaces/workspace_form.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        WorkspaceMember.objects.create(
            workspace=self.object,
            user=self.request.user,
            role=WorkspaceMember.Role.OWNER
        )
        return response
    
    def get_success_url(self):
        return reverse_lazy('workspaces:workspace_detail', kwargs={'slug': self.object.slug})


class WorkspaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Workspace
    form_class = WorkspaceForm
    template_name = 'workspaces/workspace_form.html'
    
    def get_success_url(self):
        return reverse_lazy('workspaces:workspace_detail', kwargs={'slug': self.object.slug})


class WorkspaceDeleteView(LoginRequiredMixin, DeleteView):
    model = Workspace
    template_name = 'workspaces/workspace_confirm_delete.html'
    success_url = reverse_lazy('workspaces:workspace_list')

