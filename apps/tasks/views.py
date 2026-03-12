from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Task
from .forms import TaskForm
from apps.boards.models import BoardList


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.board_list = get_object_or_404(BoardList, pk=self.kwargs['list_pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['board'] = self.board_list.board
        return kwargs
    
    def form_valid(self, form):
        form.instance.list = self.board_list
        form.instance.board = self.board_list.board
        form.instance.created_by = self.request.user
        max_position = Task.objects.filter(list=self.board_list).count()
        form.instance.position = max_position
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('boards:board_detail', kwargs={'pk': self.board_list.board.pk})


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['board'] = self.object.board
        return kwargs
    
    def get_success_url(self):
        return reverse_lazy('tasks:task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('boards:board_detail', kwargs={'pk': self.object.board.pk})


class TaskToggleCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.is_completed():
            task.mark_incomplete()
        else:
            task.mark_completed()
        return redirect('tasks:task_detail', pk=task.pk)


@method_decorator(csrf_exempt, name='dispatch')
class TaskMoveView(LoginRequiredMixin, View):
    """Move task to different list and update position"""
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        new_list_id = request.POST.get('list_id')
        new_position = request.POST.get('position', 0)
        
        try:
            new_list = BoardList.objects.get(pk=new_list_id)
            
            # Check if user has access to this board
            if not new_list.board.workspace.has_member(request.user):
                return JsonResponse({'success': False, 'error': 'Sin permiso'}, status=403)
            
            old_list = task.list
            
            # Update task list and position
            task.list = new_list
            task.position = int(new_position)
            task.save()
            
            # Reorder tasks in old list
            old_tasks = Task.objects.filter(list=old_list).order_by('position')
            for idx, t in enumerate(old_tasks):
                if t.position != idx:
                    t.position = idx
                    t.save()
            
            # Reorder tasks in new list
            new_tasks = Task.objects.filter(list=new_list).order_by('position')
            for idx, t in enumerate(new_tasks):
                if t.position != idx:
                    t.position = idx
                    t.save()
            
            return JsonResponse({'success': True})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)


