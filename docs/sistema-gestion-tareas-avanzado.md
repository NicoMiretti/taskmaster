# Sistema de Gestión de Tareas Avanzado - Django

## 📋 Descripción del Proyecto

Sistema completo de gestión de tareas estilo **Trello/Asana** con funcionalidades avanzadas de colaboración, priorización y organización. Incluye tableros compartidos, asignación de tareas, comentarios en tiempo real, etiquetas, fechas límite y sistema de notificaciones.

---

## 🎯 Funcionalidades Principales

### 1. Gestión de Usuarios
- Registro y autenticación de usuarios
- Perfiles de usuario con foto, bio y configuración
- Roles: Admin, Manager, Usuario Regular
- Recuperación de contraseña por email
- Configuración de preferencias (tema, notificaciones)

### 2. Workspaces (Espacios de Trabajo)
- Crear workspaces para organizar proyectos
- Invitar miembros al workspace por email
- Permisos por workspace (owner, admin, member, viewer)
- Dashboard de workspace con métricas

### 3. Tableros y Listas
- Crear tableros dentro de cada workspace
- Listas personalizables (ej: To Do, In Progress, Done)
- Arrastrar y soltar tareas entre listas (drag & drop)
- Plantillas de tableros pre-configuradas
- Archivar/desarchivar tableros

### 4. Tareas (Core)
- Título, descripción enriquecida (Markdown o WYSIWYG)
- Fecha de creación, fecha límite, fecha de inicio
- Prioridad (Baja, Media, Alta, Crítica)
- Estado personalizable según lista
- Asignar múltiples usuarios a una tarea
- Subtareas con checkboxes
- Adjuntar archivos (imágenes, PDFs, docs)
- Tags/etiquetas con colores
- Estimación de tiempo y tiempo trabajado
- Dependencias entre tareas

### 5. Colaboración
- Comentarios en tareas con menciones (@usuario)
- Historial de actividad de la tarea
- Notificaciones en tiempo real (con Django Channels opcional)
- Reacciones a comentarios (emoji)
- Observadores de tareas (watchers)

### 6. Búsqueda y Filtros
- Búsqueda full-text de tareas
- Filtrar por: asignado, etiquetas, prioridad, fecha, estado
- Vistas personalizadas guardadas
- Ordenar por: fecha, prioridad, alfabético

### 7. Reportes y Analytics
- Gráficos de tareas por estado
- Tareas completadas por usuario
- Burndown chart (opcional)
- Exportar reportes a PDF/Excel
- Métricas de productividad del equipo

### 8. Notificaciones
- Email para tareas asignadas
- Recordatorios de fechas límite
- Notificaciones in-app
- Resumen diario/semanal por email

---

## 🗄️ Estructura de Base de Datos

### Modelos Principales

```python
# users/models.py
User (AbstractUser extendido)
- username
- email
- first_name, last_name
- avatar (ImageField)
- bio (TextField)
- created_at, updated_at
- email_verified
- preferred_theme (light/dark)

UserProfile
- user (OneToOne)
- timezone
- language
- notifications_enabled
- email_digest_frequency

# workspaces/models.py
Workspace
- name
- slug
- description
- owner (FK User)
- created_at
- is_active

WorkspaceMember
- workspace (FK)
- user (FK)
- role (choices: owner, admin, member, viewer)
- joined_at
- invited_by (FK User)

# boards/models.py
Board
- workspace (FK)
- name
- description
- created_by (FK User)
- created_at
- is_archived
- background_color
- is_template

BoardList
- board (FK)
- name
- position (IntegerField para ordenar)
- color
- is_archived

# tasks/models.py
Task
- board (FK)
- list (FK BoardList)
- title
- description (TextField/RichTextField)
- created_by (FK User)
- assigned_to (M2M User through TaskAssignment)
- priority (choices: low, medium, high, critical)
- status (calculated from list)
- due_date
- start_date
- estimated_hours
- actual_hours
- position (para ordenar dentro de lista)
- is_archived
- completed_at
- created_at, updated_at

TaskAssignment
- task (FK)
- user (FK)
- assigned_by (FK User)
- assigned_at

Subtask
- task (FK)
- title
- is_completed
- position
- created_at

Tag
- workspace (FK)
- name
- color
- created_by

TaskTag
- task (FK)
- tag (FK)

TaskDependency
- task (FK)
- depends_on (FK Task)
- dependency_type (blocks, blocked_by)

Attachment
- task (FK)
- file (FileField)
- uploaded_by (FK User)
- uploaded_at
- file_name
- file_size

Comment
- task (FK)
- user (FK)
- content (TextField)
- created_at, updated_at
- edited
- parent (FK Comment, for replies)

CommentReaction
- comment (FK)
- user (FK)
- emoji

TaskActivity
- task (FK)
- user (FK)
- action_type (created, updated, commented, assigned, etc)
- description
- created_at
- metadata (JSONField)

TaskWatcher
- task (FK)
- user (FK)
- added_at

# notifications/models.py
Notification
- user (FK)
- notification_type
- title
- message
- link
- is_read
- created_at
- related_task (FK, nullable)
```

---

## 📁 Estructura del Proyecto Django

```
taskmaster/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── config/                      # Configuración principal
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py              # Settings comunes
│   │   ├── development.py       # Settings de desarrollo
│   │   └── production.py        # Settings de producción
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py                  # Para WebSockets (opcional)
│
├── apps/                        # Aplicaciones del proyecto
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── serializers.py       # Para API REST
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── signals.py
│   │   ├── managers.py
│   │   └── tests/
│   │
│   ├── workspaces/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   ├── permissions.py       # Permisos personalizados
│   │   └── tests/
│   │
│   ├── boards/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── tests/
│   │
│   ├── tasks/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── filters.py           # Django-filter
│   │   ├── services.py          # Lógica de negocio
│   │   └── tests/
│   │
│   ├── notifications/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── tasks.py             # Celery tasks
│   │   └── utils.py
│   │
│   └── core/
│       ├── mixins.py            # Mixins reutilizables
│       ├── decorators.py
│       ├── utils.py
│       └── middleware.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── users/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── workspaces/
│   │   ├── workspace_list.html
│   │   ├── workspace_detail.html
│   │   └── workspace_form.html
│   ├── boards/
│   │   ├── board_detail.html
│   │   └── board_list.html
│   ├── tasks/
│   │   ├── task_detail.html
│   │   ├── task_form.html
│   │   └── components/
│   │       ├── task_card.html
│   │       ├── comment_list.html
│   │       └── subtask_list.html
│   └── partials/
│       ├── navbar.html
│       ├── sidebar.html
│       └── notifications_dropdown.html
│
├── static/
│   ├── css/
│   │   ├── styles.css
│   │   └── themes/
│   │       ├── light.css
│   │       └── dark.css
│   ├── js/
│   │   ├── main.js
│   │   ├── task_board.js        # Drag & drop
│   │   ├── notifications.js
│   │   └── htmx_config.js       # Si usas HTMX
│   └── images/
│
├── media/                        # Archivos subidos
│   ├── avatars/
│   ├── attachments/
│   └── exports/
│
└── tests/                        # Tests de integración
    ├── test_workflows.py
    └── test_permissions.py
```

---

## 🛣️ URLs y Vistas Principales

### Estructura de URLs

```python
# config/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('users/', include('apps.users.urls')),
    path('workspaces/', include('apps.workspaces.urls')),
    path('boards/', include('apps.boards.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('api/v1/', include('api.urls')),  # API REST
]

# apps/workspaces/urls.py
urlpatterns = [
    path('', WorkspaceListView.as_view(), name='workspace_list'),
    path('create/', WorkspaceCreateView.as_view(), name='workspace_create'),
    path('<slug:slug>/', WorkspaceDetailView.as_view(), name='workspace_detail'),
    path('<slug:slug>/settings/', WorkspaceSettingsView.as_view(), name='workspace_settings'),
    path('<slug:slug>/members/', WorkspaceMembersView.as_view(), name='workspace_members'),
    path('<slug:slug>/invite/', InviteMemberView.as_view(), name='invite_member'),
]

# apps/boards/urls.py
urlpatterns = [
    path('<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('create/', BoardCreateView.as_view(), name='board_create'),
    path('<int:pk>/lists/create/', ListCreateView.as_view(), name='list_create'),
    path('<int:pk>/archive/', ArchiveBoardView.as_view(), name='board_archive'),
]

# apps/tasks/urls.py
urlpatterns = [
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/assign/', AssignTaskView.as_view(), name='task_assign'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('<int:pk>/attach/', AttachFileView.as_view(), name='attach_file'),
    path('<int:pk>/move/', MoveTaskView.as_view(), name='move_task'),
    path('search/', TaskSearchView.as_view(), name='task_search'),
]
```

### Vistas Clave

```python
# apps/boards/views.py
class BoardDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Vista principal del tablero con drag & drop"""
    model = Board
    template_name = 'boards/board_detail.html'
    
    def test_func(self):
        # Verificar permisos de workspace
        return self.get_object().workspace.has_member(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = self.object.lists.prefetch_related('tasks')
        context['members'] = self.object.workspace.members.all()
        context['tags'] = self.object.workspace.tags.all()
        return context

# apps/tasks/views.py
class TaskDetailView(LoginRequiredMixin, DetailView):
    """Vista detallada de tarea con comentarios y actividad"""
    model = Task
    template_name = 'tasks/task_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.select_related('user')
        context['activity'] = self.object.activities.select_related('user')[:20]
        context['subtasks'] = self.object.subtasks.all()
        context['attachments'] = self.object.attachments.all()
        return context

class TaskSearchView(LoginRequiredMixin, ListView):
    """Búsqueda y filtrado avanzado"""
    model = Task
    template_name = 'tasks/search.html'
    paginate_by = 20
    
    def get_queryset(self):
        qs = Task.objects.filter(
            board__workspace__members__user=self.request.user
        )
        
        # Aplicar filtros
        if q := self.request.GET.get('q'):
            qs = qs.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
        
        if priority := self.request.GET.get('priority'):
            qs = qs.filter(priority=priority)
        
        if assigned := self.request.GET.get('assigned_to'):
            qs = qs.filter(assigned_to__id=assigned)
        
        if tags := self.request.GET.getlist('tags'):
            qs = qs.filter(tags__id__in=tags)
        
        return qs.distinct()
```

---

## 🎨 Frontend y UX

### Tecnologías Recomendadas

1. **Framework CSS:**
   - Bootstrap 5 (fácil y rápido)
   - Tailwind CSS (más personalizable)
   - Bulma (ligero y moderno)

2. **JavaScript:**
   - **Alpine.js** - Para interactividad ligera
   - **HTMX** - Actualizar UI sin recargar página
   - **SortableJS** - Drag & drop de tareas
   - **Chart.js** - Gráficos y reportes

3. **Iconos:**
   - Font Awesome
   - Heroicons
   - Bootstrap Icons

### Características de UI

- **Drag & Drop:** Arrastrar tareas entre listas
- **Modal Dialogs:** Para crear/editar tareas rápido
- **Autocomplete:** En búsqueda y menciones
- **Infinite Scroll:** Para listas largas de tareas
- **Toast Notifications:** Feedback de acciones
- **Dark Mode:** Tema oscuro/claro
- **Responsive:** Mobile-first design

### Ejemplo de Template Base

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TaskMaster{% endblock %}</title>
    
    <!-- CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% include 'partials/navbar.html' %}
    
    <div class="container-fluid">
        <div class="row">
            <!-- Sidebar -->
            <nav class="col-md-2 d-none d-md-block bg-light sidebar">
                {% include 'partials/sidebar.html' %}
            </nav>
            
            <!-- Main content -->
            <main class="col-md-10 ms-sm-auto px-md-4">
                {% if messages %}
                    {% for message in messages %}
                        <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                            {{ message }}
                            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                        </div>
                    {% endfor %}
                {% endif %}
                
                {% block content %}{% endblock %}
            </main>
        </div>
    </div>
    
    <!-- JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"></script>
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## 🔐 Sistema de Permisos

### Niveles de Acceso

```python
# apps/workspaces/permissions.py
class WorkspacePermission:
    """
    Workspace Owner: Puede todo
    Workspace Admin: Puede gestionar miembros y tableros
    Member: Puede crear tareas y comentar
    Viewer: Solo lectura
    """
    
    @staticmethod
    def can_manage_members(user, workspace):
        membership = workspace.members.filter(user=user).first()
        return membership and membership.role in ['owner', 'admin']
    
    @staticmethod
    def can_create_board(user, workspace):
        membership = workspace.members.filter(user=user).first()
        return membership and membership.role != 'viewer'
    
    @staticmethod
    def can_edit_task(user, task):
        # Puede editar si es creador, asignado, o admin del workspace
        return (
            task.created_by == user or
            task.assigned_to.filter(id=user.id).exists() or
            WorkspacePermission.can_manage_members(user, task.board.workspace)
        )
```

### Decoradores Personalizados

```python
# apps/core/decorators.py
def workspace_member_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        workspace_slug = kwargs.get('slug')
        workspace = get_object_or_404(Workspace, slug=workspace_slug)
        
        if not workspace.has_member(request.user):
            messages.error(request, "No tienes acceso a este workspace")
            return redirect('workspace_list')
        
        return view_func(request, *args, **kwargs)
    return wrapper
```

---

## 🚀 Funcionalidades Avanzadas

### 1. API REST con Django REST Framework

```python
# api/serializers.py
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'

# api/views.py
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['priority', 'list', 'assigned_to']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority']
    
    def get_queryset(self):
        return Task.objects.filter(
            board__workspace__members__user=self.request.user
        )
```

### 2. Notificaciones en Tiempo Real (WebSockets)

```python
# config/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/notifications/', NotificationConsumer.as_asgi()),
        ])
    ),
})

# apps/notifications/consumers.py
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope["user"].id
        self.group_name = f"notifications_{self.user_id}"
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
    
    async def notification_message(self, event):
        await self.send(text_data=json.dumps(event["message"]))
```

### 3. Tareas Asíncronas con Celery

```python
# apps/notifications/tasks.py
from celery import shared_task

@shared_task
def send_due_date_reminders():
    """Enviar recordatorios de tareas próximas a vencer"""
    tomorrow = timezone.now() + timedelta(days=1)
    tasks = Task.objects.filter(
        due_date__date=tomorrow.date(),
        is_archived=False
    ).select_related('created_by')
    
    for task in tasks:
        for user in task.assigned_to.all():
            send_email(
                subject=f"Recordatorio: {task.title} vence mañana",
                to=user.email,
                template='emails/due_date_reminder.html',
                context={'task': task, 'user': user}
            )

@shared_task
def send_daily_digest(user_id):
    """Enviar resumen diario de actividad"""
    user = User.objects.get(id=user_id)
    tasks_assigned = Task.objects.filter(
        assigned_to=user,
        is_archived=False
    ).count()
    
    # ... lógica de resumen
```

### 4. Importación/Exportación de Datos

```python
# apps/tasks/services.py
class TaskExporter:
    @staticmethod
    def export_to_csv(workspace_id):
        tasks = Task.objects.filter(
            board__workspace_id=workspace_id
        ).select_related('created_by', 'list')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tasks.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Título', 'Estado', 'Prioridad', 'Asignado', 'Fecha Límite'])
        
        for task in tasks:
            writer.writerow([
                task.title,
                task.list.name,
                task.get_priority_display(),
                ', '.join([u.username for u in task.assigned_to.all()]),
                task.due_date
            ])
        
        return response
```

---

## 🧪 Testing

### Estructura de Tests

```python
# apps/tasks/tests/test_models.py
class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test123')
        self.workspace = Workspace.objects.create(name='Test WS', owner=self.user)
        self.board = Board.objects.create(workspace=self.workspace, name='Test Board')
        self.list = BoardList.objects.create(board=self.board, name='To Do')
    
    def test_task_creation(self):
        task = Task.objects.create(
            board=self.board,
            list=self.list,
            title='Test Task',
            created_by=self.user
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertIsNotNone(task.created_at)
    
    def test_task_assignment(self):
        task = Task.objects.create(...)
        task.assigned_to.add(self.user)
        self.assertIn(self.user, task.assigned_to.all())

# apps/tasks/tests/test_views.py
class TaskViewsTest(TestCase):
    def test_task_create_view_requires_login(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_task_create_authenticated(self):
        self.client.login(username='test', password='test123')
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'board': self.board.id,
            'list': self.list.id,
        })
        self.assertEqual(Task.objects.count(), 1)
```

---

## 📦 Dependencias (requirements.txt)

```txt
# Core
Django==5.0.1
python-decouple==3.8

# Database
psycopg2-binary==2.9.9  # PostgreSQL

# API
djangorestframework==3.14.0
django-filter==23.5
django-cors-headers==4.3.1

# Authentication
djangorestframework-simplejwt==5.3.1

# Files & Images
Pillow==10.2.0
django-storages==1.14.2  # Para S3/Azure

# Tasks Queue
celery==5.3.6
redis==5.0.1
django-celery-beat==2.5.0  # Tareas periódicas

# WebSockets (opcional)
channels==4.0.0
channels-redis==4.1.0

# Utils
django-extensions==3.2.3
django-debug-toolbar==4.2.0
python-slugify==8.0.1
django-crispy-forms==2.1
crispy-bootstrap5==2.0.0

# Testing
pytest==7.4.4
pytest-django==4.7.0
factory-boy==3.3.0
faker==22.0.0

# Monitoring
sentry-sdk==1.39.2

# Markdown (opcional)
markdown==3.5.1
bleach==6.1.0  # Para sanitizar HTML
```

---

## ⚙️ Configuración Inicial

### 1. Variables de Entorno (.env)

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=taskmaster_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Email
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password

# Redis
REDIS_URL=redis://localhost:6379/0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Media/Static
MEDIA_URL=/media/
STATIC_URL=/static/
```

### 2. Settings Base

```python
# config/settings/base.py
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'rest_framework',
    'django_filters',
    'crispy_forms',
    'crispy_bootstrap5',
    
    # Local apps
    'apps.users',
    'apps.workspaces',
    'apps.boards',
    'apps.tasks',
    'apps.notifications',
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'users.User'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
```

---

## 🚦 Roadmap de Implementación

### Fase 1: Setup y Autenticación (1 semana)
- [ ] Configurar proyecto Django
- [ ] Modelo de Usuario personalizado
- [ ] Sistema de registro/login
- [ ] Perfiles de usuario
- [ ] Recovery de contraseña

### Fase 2: Workspaces y Tableros (1 semana)
- [ ] Modelo de Workspace
- [ ] CRUD de workspaces
- [ ] Invitar miembros
- [ ] Sistema de permisos básico
- [ ] Modelo de Board y BoardList
- [ ] Vista de tablero

### Fase 3: Tareas Core (1.5 semanas)
- [ ] Modelo de Task completo
- [ ] Crear/editar/eliminar tareas
- [ ] Asignar usuarios
- [ ] Tags y prioridades
- [ ] Subtareas
- [ ] Adjuntar archivos

### Fase 4: Colaboración (1 semana)
- [ ] Sistema de comentarios
- [ ] Menciones de usuarios
- [ ] Actividad de tareas
- [ ] Watchers

### Fase 5: Búsqueda y Filtros (3-4 días)
- [ ] Búsqueda full-text
- [ ] Filtros avanzados
- [ ] Vistas guardadas

### Fase 6: Notificaciones (1 semana)
- [ ] Modelo de notificaciones
- [ ] Notificaciones in-app
- [ ] Emails de notificación
- [ ] Configuración de preferencias

### Fase 7: Analytics y Reportes (3-4 días)
- [ ] Dashboard con métricas
- [ ] Gráficos
- [ ] Exportar a PDF/CSV

### Fase 8: UI/UX Avanzado (1 semana)
- [ ] Drag & drop
- [ ] Modal dialogs
- [ ] Dark mode
- [ ] Responsive design

### Fase 9: API REST (3-4 días)
- [ ] Serializers
- [ ] ViewSets
- [ ] Documentación (Swagger)

### Fase 10: Testing y Deploy (1 semana)
- [ ] Tests unitarios
- [ ] Tests de integración
- [ ] Configuración de producción
- [ ] Deploy (Heroku/Railway/DigitalOcean)

**Tiempo estimado total:** 8-10 semanas

---

## 📚 Recursos Adicionales

### Documentación
- [Django Docs](https://docs.djangoproject.com/)
- [DRF Docs](https://www.django-rest-framework.org/)
- [Celery Docs](https://docs.celeryproject.org/)
- [Channels Docs](https://channels.readthedocs.io/)

### Tutoriales Recomendados
- Django for Beginners - William Vincent
- Two Scoops of Django
- Real Python Django Tutorials

### Herramientas de Desarrollo
- PostgreSQL / pgAdmin
- Redis / RedisInsight
- Postman (API testing)
- VS Code con extensiones Django

---

## 🎓 Criterios de Evaluación Académica

### Aspectos Técnicos (60%)
- **Modelos:** Correcta estructura y relaciones (15%)
- **Vistas:** Implementación de lógica de negocio (15%)
- **Templates:** UI funcional y responsive (10%)
- **Autenticación:** Sistema de permisos robusto (10%)
- **API:** Endpoints RESTful funcionales (10%)

### Funcionalidad (20%)
- Todas las features core implementadas
- Manejo de errores y validaciones
- Performance aceptable

### Código (10%)
- Código limpio y organizado
- Comentarios cuando sea necesario
- Buenas prácticas de Django

### Testing (5%)
- Tests unitarios
- Cobertura razonable

### Documentación (5%)
- README completo
- Instrucciones de instalación
- Guía de uso

---

## 💡 Tips para el Desarrollo

1. **Empezar simple:** Implementa primero las funcionalidades core antes que las avanzadas
2. **Commits frecuentes:** Usa Git desde el inicio
3. **Testing continuo:** No dejes los tests para el final
4. **Refactorizar:** Mejora el código constantemente
5. **Pedir ayuda:** Usa Stack Overflow, Django Discord, etc.
6. **Documentar:** Escribe comentarios y README mientras desarrollas

---

**¡Éxito con tu proyecto!** 🚀
