# TaskMaster v1.0 Development Guide

## Quick Start

### 1. First Time Setup
```bash
# Windows PowerShell
.\setup.ps1

# Or manually:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
```

### 2. Create Superuser
```bash
python manage.py createsuperuser
```

### 3. Run Development Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000

## Project Structure

```
taskmaster/
├── apps/                   # Django applications
│   ├── users/             # User authentication & profiles
│   ├── workspaces/        # Workspace management
│   ├── boards/            # Boards and lists
│   ├── tasks/             # Task management
│   └── core/              # Core utilities
├── config/                # Django configuration
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS)
├── media/                 # User uploads
└── docs/                  # Project documentation
```

## Key Models

### User
- Custom user model extending AbstractUser
- Fields: username, email, bio, avatar

### Workspace
- Container for boards and projects
- Has members with roles (owner, admin, member, viewer)

### Board
- Belongs to a workspace
- Contains lists (Kanban columns)

### BoardList
- Column in a Kanban board
- Contains tasks

### Task
- Belongs to a board and list
- Has priority, due date, assignees
- Can be marked as completed

## Development Workflow

### Creating a New App Feature

1. **Add model** in `apps/<app>/models.py`
2. **Create migration**: `python manage.py makemigrations`
3. **Apply migration**: `python manage.py migrate`
4. **Register in admin**: `apps/<app>/admin.py`
5. **Create form**: `apps/<app>/forms.py`
6. **Create view**: `apps/<app>/views.py`
7. **Add URL**: `apps/<app>/urls.py`
8. **Create template**: `templates/<app>/<template>.html`

### Running Tests
```bash
python manage.py test
```

### Creating Test Data
```bash
python manage.py shell
```

```python
from apps.users.models import User
from apps.workspaces.models import Workspace, WorkspaceMember
from apps.boards.models import Board, BoardList
from apps.tasks.models import Task

# Create user
user = User.objects.create_user('demo', 'demo@example.com', 'demo123')

# Create workspace
ws = Workspace.objects.create(name='Mi Proyecto', owner=user)
WorkspaceMember.objects.create(workspace=ws, user=user, role='owner')

# Create board
board = Board.objects.create(workspace=ws, name='Sprint 1', created_by=user)

# Create lists
list1 = BoardList.objects.create(board=board, name='Por Hacer', position=0)
list2 = BoardList.objects.create(board=board, name='En Progreso', position=1)

# Create task
task = Task.objects.create(
    board=board,
    list=list1,
    title='Mi primera tarea',
    created_by=user,
    priority='high'
)
task.assigned_to.add(user)
```

## Common Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

# Open Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Check for issues
python manage.py check
```

## Adding New Features (Roadmap)

### v1.1 Features to Implement

1. **Comments System**
   - Model: `Comment` in tasks app
   - Fields: task, user, content, created_at
   - View: AJAX comment posting
   - Template: Comment list in task detail

2. **Tags System**
   - Model: `Tag` in tasks app
   - Many-to-many with Task
   - Color field for visual distinction

3. **Search Functionality**
   - Add search form in navbar
   - Filter tasks by title/description
   - Use Q objects for complex queries

4. **Notifications**
   - Model: `Notification` app
   - Trigger on task assignment, mentions
   - Display in dropdown menu

## Troubleshooting

### Database locked
```bash
# Close all Django processes and try again
python manage.py migrate
```

### Static files not loading
```bash
python manage.py collectstatic
```

### Import errors
```bash
# Make sure apps are properly configured in settings.py
# Check that apps have __init__.py files
```

## Production Deployment

When ready for production:

1. Change `DEBUG = False` in .env
2. Set proper `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Use PostgreSQL instead of SQLite
5. Set up static file serving
6. Use Gunicorn or uWSGI
7. Set up Nginx as reverse proxy
8. Configure HTTPS

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/)

## License

Educational Project - Free to use and modify
