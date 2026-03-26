# Guía para el Video de Entrega — TaskMaster (máx. 4 minutos)

---

## Estructura sugerida del video

| Segmento | Duración |
|----------|----------|
| Presentación del proyecto y Git | ~40 seg |
| Contenido estático en Django | ~30 seg |
| Formularios (Forms) en acción | ~1 min 30 seg |
| Flujo principal de la app | ~1 min |
| Cierre | ~20 seg |

---

## Paso 1 — Presentación del proyecto y Git (~40 seg)

1. Abrir GitHub (o la plataforma usada) y mostrar el repositorio del grupo.
2. Señalar:
   - El nombre del repo y que está **compartido con todo el grupo** (pestaña *Settings > Collaborators* o los *Contributors*).
   - La lista de commits para mostrar historial de trabajo.
3. Decir brevemente qué es el proyecto:  
   > *"TaskMaster es una app de gestión de tareas construida con Python y Django. Permite crear workspaces, tableros tipo Kanban y tareas asignables."*

---

## Paso 2 — Contenido estático en Django (~30 seg)

1. Mostrar en el editor (o en el navegador con DevTools) que la app carga archivos estáticos reales:
   - `static/css/styles.css` → estilos personalizados.
   - `static/js/board.js` y `static/js/darkmode.js` → JavaScript del tablero y modo oscuro.
2. En el código, mostrar un template (p. ej. `templates/base.html`) donde aparece `{% load static %}` y una línea como `{% static 'css/styles.css' %}`.
3. En `config/settings.py` señalar las líneas:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

4. **Demostración visual**: activar el modo oscuro en la app en vivo (usa `darkmode.js`) para mostrar que el JS estático funciona.

---

## Paso 3 — Formularios Django en acción (~1 min 30 seg)

El proyecto tiene **6 formularios reales** en Django. Mostrar al menos 2-3:

### 3a. Registro de usuario — `UserRegisterForm`
- Ir a la URL `/register/`.
- Mostrar el formulario en pantalla (campos: username, email, contraseña, confirmación).
- Completarlo y registrar un usuario nuevo en vivo.
- Señalar en el código `apps/users/forms.py` que extiende `UserCreationForm` con campo extra de email.

### 3b. Crear Workspace — `WorkspaceForm`
- Tras el login, ir a *"Nuevo Workspace"*.
- Completar nombre y descripción y guardar.
- Señalar `apps/workspaces/forms.py`.

### 3c. Crear Tarea — `TaskForm` (el más completo)
- Dentro de un tablero, crear una tarea con título, descripción, prioridad, fecha de vencimiento y asignado a.
- Destacar que el widget de fecha usa `type="datetime-local"`:
```python
'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
```
- Señalar en `apps/tasks/forms.py` que el queryset de `assigned_to` se filtra dinámicamente según el workspace.

---

## Paso 4 — Flujo principal de la app (~1 min)

Mostrar el recorrido completo en el navegador:

1. **Login** → redirige automáticamente a lista de workspaces.
2. **Workspace** → ver el workspace creado, entrar a él.
3. **Tablero** → mostrar las columnas *"Por Hacer / En Progreso / Completado"* (creadas automáticamente al hacer el board).
4. **Drag & Drop** de una tarea entre columnas (funcionalidad de `board.js`).
5. **Detalle de tarea** → mostrar campos completos de la tarea creada.

---

## Paso 5 — Cierre (~20 seg)

- Mencionar la tecnología: *Python 3 + Django + Bootstrap 5 + SQLite*.
- Mostrar brevemente el `README.md` con instrucciones de instalación.
- Agradecer y cortar.

---

## Checklist antes de grabar

- [ ] El servidor corre con `python manage.py runserver`
- [ ] Hay al menos un usuario de prueba creado (o crearlo en vivo)
- [ ] Hay un workspace y un tablero con tareas de ejemplo
- [ ] El repositorio en GitHub está actualizado con el último commit
- [ ] Los colaboradores del grupo están visibles en GitHub
- [ ] `static/` cargando correctamente (sin errores 404 en consola)
- [ ] Modo oscuro funciona al hacer clic en el botón

---

## URLs útiles para el video

| Pantalla | URL |
|----------|-----|
| Home / Login | `http://127.0.0.1:8000/` |
| Registro | `http://127.0.0.1:8000/users/register/` |
| Lista de workspaces | `http://127.0.0.1:8000/workspaces/` |
| Nuevo workspace | `http://127.0.0.1:8000/workspaces/create/` |
| Detalle de tablero | `http://127.0.0.1:8000/boards/<id>/` |
