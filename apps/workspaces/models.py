from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Workspace(models.Model):
    """Workspace for organizing projects and boards"""
    name = models.CharField(_('nombre'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    description = models.TextField(_('descripción'), blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_workspaces',
        verbose_name=_('propietario')
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='WorkspaceMember',
        related_name='workspaces',
        verbose_name=_('miembros')
    )
    created_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    is_active = models.BooleanField(_('activo'), default=True)
    
    class Meta:
        verbose_name = _('workspace')
        verbose_name_plural = _('workspaces')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def has_member(self, user):
        """Check if user is a member of this workspace"""
        return self.members.filter(id=user.id).exists()


class WorkspaceMember(models.Model):
    """Relationship between Workspace and Users with roles"""
    
    class Role(models.TextChoices):
        OWNER = 'owner', _('Propietario')
        ADMIN = 'admin', _('Administrador')
        MEMBER = 'member', _('Miembro')
        VIEWER = 'viewer', _('Observador')
    
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='workspace_members'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='workspace_memberships'
    )
    role = models.CharField(
        _('rol'),
        max_length=10,
        choices=Role.choices,
        default=Role.MEMBER
    )
    joined_at = models.DateTimeField(_('fecha de ingreso'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('miembro del workspace')
        verbose_name_plural = _('miembros del workspace')
        unique_together = ['workspace', 'user']
    
    def __str__(self):
        return f'{self.user.username} - {self.workspace.name} ({self.role})'

