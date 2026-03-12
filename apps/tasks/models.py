from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Task(models.Model):
    """Task within a board list"""
    
    class Priority(models.TextChoices):
        LOW = 'low', _('Baja')
        MEDIUM = 'medium', _('Media')
        HIGH = 'high', _('Alta')
        CRITICAL = 'critical', _('Crítica')
    
    board = models.ForeignKey(
        'boards.Board',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name=_('tablero')
    )
    list = models.ForeignKey(
        'boards.BoardList',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name=_('lista')
    )
    title = models.CharField(_('título'), max_length=255)
    description = models.TextField(_('descripción'), blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_tasks',
        verbose_name=_('creado por')
    )
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='assigned_tasks',
        blank=True,
        verbose_name=_('asignado a')
    )
    priority = models.CharField(
        _('prioridad'),
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    due_date = models.DateTimeField(_('fecha límite'), null=True, blank=True)
    position = models.IntegerField(_('posición'), default=0)
    is_archived = models.BooleanField(_('archivada'), default=False)
    completed_at = models.DateTimeField(_('completada en'), null=True, blank=True)
    created_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    updated_at = models.DateTimeField(_('última actualización'), auto_now=True)
    
    class Meta:
        verbose_name = _('tarea')
        verbose_name_plural = _('tareas')
        ordering = ['position', '-created_at']
    
    def __str__(self):
        return self.title
    
    def is_completed(self):
        """Check if task is marked as completed"""
        return self.completed_at is not None
    
    def mark_completed(self):
        """Mark task as completed"""
        from django.utils import timezone
        if not self.completed_at:
            self.completed_at = timezone.now()
            self.save()
    
    def mark_incomplete(self):
        """Mark task as incomplete"""
        self.completed_at = None
        self.save()

