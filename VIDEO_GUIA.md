# Guía para el Video de Entrega — TaskMaster (máx. 4 minutos)

---

## Estructura sugerida del video

| Segmento | Duración |
|----------|----------|
| Presentación del proyecto y Git | ~40 seg |
| Cómo funciona Django (la comunicación) | ~40 seg |
| Contenido estático en Django | ~30 seg |
| Formularios (Forms) en acción | ~1 min 20 seg |
| Flujo principal de la app | ~30 seg |
| Cierre | ~20 seg |

---

## Paso 1 — Presentación del proyecto y Git (~40 seg)

### Qué hacer
1. Abrir `https://github.com/NicoMiretti/taskmaster` en el navegador.
2. Señalar la pestaña **Contributors** o **Settings > Collaborators** para mostrar que está compartido con el grupo.
3. Hacer clic en **Commits** y mostrar el historial de cambios.

### Qué decir
> *"Este es nuestro repositorio de GitHub. Acá se puede ver el historial de commits del equipo y que el repo está compartido con todos los integrantes del grupo. El proyecto es TaskMaster, una aplicación de gestión de tareas construida con Python y Django."*

---

## Paso 2 — Cómo funciona Django: la comunicación entre partes (~40 seg)

Esta es la parte más importante para explicar al profe. Django sigue el patrón **MVT** (Model - View - Template). Así funciona cada vez que el usuario hace algo en la app:

```
Navegador  →  URL  →  View  →  Model (base de datos)  →  Template (HTML)  →  Navegador
```

### Ejemplo concreto: el usuario crea una tarea

1. **El navegador** manda un POST a `/tasks/create/1/` con los datos del formulario.
2. **`config/urls.py`** recibe la URL y la delega a `apps/tasks/urls.py`.
3. **`apps/tasks/urls.py`** la dirige a `TaskCreateView` (en `views.py`).
4. **La View** (`apps/tasks/views.py`) valida el formulario, guarda la tarea en la base de datos usando el **Model** (`Task`), y redirige al tablero.
5. El navegador carga el tablero y Django renderiza el **Template** `boards/board_detail.html` con los datos actualizados.

### Qué mostrar en el código (abrí estos 3 archivos en el editor)

**Archivo 1 — `apps/tasks/views.py`** (mostrar `TaskCreateView`):
```python
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task               # ← conecta con la base de datos
    form_class = TaskForm      # ← usa el formulario
    template_name = 'tasks/task_form.html'  # ← elige el HTML a mostrar

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # ← agrega datos automáticamente
        return super().form_valid(form)
```
> *"La View es el 'cerebro': recibe el pedido, procesa los datos y decide qué HTML mostrar."*

**Archivo 2 — `apps/tasks/models.py`** (mostrar el modelo `Task`):
> *"El Model define la estructura de la tabla en la base de datos. Django la crea automáticamente con `makemigrations`."*

**Archivo 3 — `templates/tasks/task_form.html`** (mostrar el template):
```html
<form method="post">
    {% csrf_token %}
    {{ form|crispy }}   ← Django genera los campos automáticamente
    <button type="submit">Guardar</button>
</form>
```
> *"El Template es el HTML. Con `{{ form|crispy }}` Django dibuja todos los campos del formulario solo. No hay que escribirlos a mano."*

---

## Paso 3 — Contenido estático en Django (~30 seg)

"Contenido estático" = archivos CSS, JS e imágenes que Django sirve directamente sin procesar.

### Qué mostrar en el código

**Archivo: `templates/base.html`** (líneas clave):
```html
{% load static %}   ← le dice a Django que vas a usar archivos estáticos
<link rel="stylesheet" href="{% static 'css/styles.css' %}">   ← CSS propio
<script src="{% static 'js/darkmode.js' %}"></script>          ← JS propio
```

**Archivo: `config/settings.py`**:
```python
STATIC_URL = '/static/'                    # ← URL pública de los estáticos
STATICFILES_DIRS = [BASE_DIR / 'static']   # ← carpeta donde están los archivos
```

### Demostración visual
- Hacer clic en el botón de modo oscuro de la app → muestra que `darkmode.js` funciona.
- Abrir DevTools (F12) → pestaña Network → filtrar por `css` o `js` → mostrar que `styles.css` carga con status 200.

---

## Paso 4 — Formularios Django en acción (~1 min 20 seg)

### 4a. Registro de usuario (`apps/users/forms.py`)

**Qué hacer:** Ir a `http://127.0.0.1:8000/users/register/` y completar el formulario en vivo.

**Qué mostrar en el código — `apps/users/forms.py`:**
```python
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)   # ← campo extra agregado
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```
> *"Este Form extiende el formulario de registro que ya trae Django y le agrega el campo email. Django valida automáticamente que las contraseñas coincidan y que el usuario no exista."*

**Qué mostrar en el código — `apps/users/views.py`:**
```python
class RegisterView(CreateView):
    form_class = UserRegisterForm         # ← usa este form
    template_name = 'users/register.html' # ← muestra este HTML
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # ← loguea automáticamente al registrarse
        return response
```

---

### 4b. Crear Tarea (`apps/tasks/forms.py`) — el más interesante

**Qué hacer:** Desde un tablero, hacer clic en "+ Agregar tarea" y llenar el formulario.

**Qué mostrar en el código — `apps/tasks/forms.py`:**
```python
class TaskForm(forms.ModelForm):
    def __init__(self, *args, board=None, **kwargs):
        super().__init__(*args, **kwargs)
        if board:
            # ← filtra los usuarios disponibles según el workspace
            self.fields['assigned_to'].queryset = board.workspace.members.all()
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
```
> *"Este formulario es dinámico: el campo 'asignado a' solo muestra los miembros del workspace actual, no todos los usuarios de la app."*

---

## Paso 5 — Flujo rápido de la app (~30 seg)

Solo mostrar el recorrido en el navegador sin explicar código:

1. Login → redirige a lista de workspaces.
2. Entrar al workspace → ver tablero.
3. Arrastrar una tarea de "Por Hacer" a "En Progreso" (drag & drop).
4. Hacer clic en la tarea → ver detalle completo.

---

## Paso 6 — Cierre (~20 seg)

> *"En resumen: usamos Python con Django siguiendo el patrón MVT. Tenemos formularios que validan datos, archivos estáticos propios, y todo el código está versionado en GitHub. Gracias."*

---

## Checklist antes de grabar

- [ ] Servidor corriendo: `python manage.py runserver`
- [ ] Tener un usuario de prueba listo (o crearlo en vivo en el video)
- [ ] Tener un workspace con un tablero y al menos 2 tareas de ejemplo
- [ ] Abrir en el editor: `apps/tasks/views.py`, `apps/tasks/forms.py`, `templates/base.html`, `config/settings.py`
- [ ] GitHub abierto en el repositorio con los Contributors visibles
- [ ] Sin errores 404 en consola del navegador para archivos estáticos

---

## URLs del video

| Pantalla | URL |
|----------|-----|
| Home / Login | `http://127.0.0.1:8000/` |
| Registro | `http://127.0.0.1:8000/users/register/` |
| Lista de workspaces | `http://127.0.0.1:8000/workspaces/` |
| Nuevo workspace | `http://127.0.0.1:8000/workspaces/create/` |
| Detalle de tablero | `http://127.0.0.1:8000/boards/<id>/` |
