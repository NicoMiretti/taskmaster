from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Board(models.Model):
    """Board containing lists and tasks"""
    workspace = models.ForeignKey(
        'workspaces.Workspace',
        on_delete=models.CASCADE,
        related_name='boards',
        verbose_name=_('workspace')
    )
    name = models.CharField(_('nombre'), max_length=100)
    description = models.TextField(_('descripción'), blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_boards',
        verbose_name=_('creado por')
    )
    created_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    is_archived = models.BooleanField(_('archivado'), default=False)
    background_color = models.CharField(
        _('color de fondo'),
        max_length=7,
        default='#0079BF',
        help_text=_('Color hexadecimal')
    )
    
    class Meta:
        verbose_name = _('tablero')
        verbose_name_plural = _('tableros')
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.workspace.name}'


class BoardList(models.Model):
    """List within a board (columns in Kanban)"""
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name='lists',
        verbose_name=_('tablero')
    )
    name = models.CharField(_('nombre'), max_length=100)
    position = models.IntegerField(_('posición'), default=0)
    color = models.CharField(
        _('color'),
        max_length=7,
        default='#EBECF0',
        help_text=_('Color hexadecimal')
    )
    is_archived = models.BooleanField(_('archivada'), default=False)
    
    class Meta:
        verbose_name = _('lista')
        verbose_name_plural = _('listas')
        ordering = ['position']
        unique_together = ['board', 'position']
    
    def __str__(self):
        return f'{self.name} - {self.board.name}'

