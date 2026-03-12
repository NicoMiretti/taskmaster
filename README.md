# TaskMaster v1.0.2

Sistema de gestión de tareas colaborativo construido con Django, diseñado para equipos que necesitan organizar proyectos con metodología Kanban.

![Version](https://img.shields.io/badge/version-1.0.2-blue)
![Django](https://img.shields.io/badge/Django-6.0.3-green)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![License](https://img.shields.io/badge/license-Educational-orange)

---

## 📋 Índice

- [¿Qué es TaskMaster?](#qué-es-taskmaster)
- [Características Principales](#características-principales)
- [¿Cómo Funciona?](#cómo-funciona)
- [Instalación](#instalación)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías](#tecnologías)
- [Roadmap](#roadmap)

---

## 🎯 ¿Qué es TaskMaster?

TaskMaster es una plataforma web de gestión de tareas tipo **Trello/Asana** que permite a equipos pequeños y medianos organizar sus proyectos de forma visual usando tableros Kanban.

### Casos de Uso

- 📚 **Equipos Universitarios**: Organizar proyectos finales con múltiples tareas
- 💼 **Startups**: Gestionar sprints de desarrollo sin herramientas complejas
- 👥 **Grupos de Trabajo**: Coordinar tareas sin perder información en chats
- 🏠 **Proyectos Personales**: Organizar tareas y seguir progreso visualmente

---

## ✨ Características Principales

### 🏢 Workspaces (Espacios de Trabajo)
Contenedores principales para organizar proyectos. Cada workspace puede tener:
- Múltiples tableros
- Miembros del equipo con diferentes roles
- Configuración independiente

**Roles disponibles:**
- **Owner (Propietario)**: Control total del workspace
- **Admin**: Puede gestionar miembros y tableros
- **Member (Miembro)**: Puede crear y editar tareas
- **Viewer (Observador)**: Solo lectura

### 📊 Tableros Kanban
Representación visual del flujo de trabajo:
- **Listas personalizables** (ej: Por Hacer, En Progreso, Completado)
- **Colores de fondo** para diferenciar proyectos
- **Creación automática** de listas predeterminadas

### ✅ Tareas
Unidad básica de trabajo con:
- **Título y descripción** detallada
- **Asignación múltiple** de usuarios
- **Prioridades** (Baja, Media, Alta, Crítica)
- **Fechas límite** para seguimiento
- **Estado de completado** marcable
- **Drag & Drop** entre listas

### 🎨 Interfaz
- **Responsive**: Funciona en desktop, tablet y móvil
- **Dark Mode**: Modo oscuro con toggle en navbar
- **Drag & Drop**: Arrastrá tareas entre listas
- **Actualización en tiempo real** de contadores

### 👤 Usuarios
- Registro e inicio de sesión
- Perfil personalizable con avatar y bio
- Vista de todos los workspaces propios

---

## 🔄 ¿Cómo Funciona?

### Flujo de Trabajo Típico

```
1. REGISTRO/LOGIN
   ↓
2. CREAR WORKSPACE
   │
   ├─→ Invitar miembros (opcional)
   │
   ↓
3. CREAR TABLERO
   │
   ├─→ Se crean 3 listas automáticamente:
   │   • Por Hacer
   │   • En Progreso  
   │   • Completado
   │
   ↓
4. CREAR TAREAS
   │
   ├─→ Asignar a miembros
   ├─→ Establecer prioridad
   ├─→ Definir fecha límite
   │
   ↓
5. GESTIONAR TAREAS
   │
   ├─→ Arrastrar entre listas (drag & drop)
   ├─→ Marcar como completadas
   ├─→ Editar información
   │
   ↓
6. SEGUIMIENTO
   └─→ Ver progreso visual en el tablero
```

### Ejemplo Práctico

**Escenario**: Equipo de 4 estudiantes desarrollando un proyecto final

1. **María (líder)** crea el workspace "Proyecto Final - Ing. Software"
2. Invita a **Juan, Pedro y Ana** como miembros
3. Crea un tablero "Sprint 1" con las listas por defecto
4. Agrega tareas:
   - "Diseñar base de datos" → asignada a Juan (Prioridad: Alta)
   - "Desarrollar API REST" → asignada a Pedro (Prioridad: Alta)
   - "Crear interfaz de login" → asignada a Ana (Prioridad: Media)
   - "Escribir documentación" → asignada a María (Prioridad: Media)

5. **Durante la semana**:
   - Juan termina la BD → arrastra su tarea a "Completado"
   - Pedro ve que Juan terminó, mueve su tarea a "En Progreso"
   - Ana encuentra un problema → cambia prioridad a "Crítica"
   - María revisa el tablero desde su celular → ve progreso en tiempo real

**Resultado**: Sin confusión, sin mensajes perdidos, progreso visible para todos.

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)

### Instalación Rápida (Windows)

```powershell
# 1. Navegar a la carpeta del proyecto
cd C:\Users\Nicolas\taskmaster

# 2. Ejecutar script de setup (recomendado)
.\setup.ps1

# O manualmente:
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
```

### Instalación Rápida (Linux/Mac)

```bash
# 1. Navegar a la carpeta del proyecto
cd /ruta/al/proyecto/taskmaster

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env

# 5. Aplicar migraciones
python manage.py migrate
```

### Crear Usuario Administrador

```bash
python manage.py createsuperuser
# Ingresá: username, email, password
```

### Ejecutar Servidor

```bash
python manage.py runserver
```

**Acceso:**
- Aplicación: http://localhost:8000
- Panel Admin: http://localhost:8000/admin

---

## 📖 Uso del Sistema

### 1. Primera Vez: Registro

1. Visitá http://localhost:8000
2. Click en **"Registrarse"**
3. Completá: username, email, contraseña
4. Serás redirigido a tus workspaces (vacío inicialmente)

### 2. Crear tu Primer Workspace

1. Click en **"Nuevo Workspace"**
2. Ingresá:
   - **Nombre**: ej. "Mi Proyecto"
   - **Descripción**: breve explicación (opcional)
3. Guardar → serás el **Owner** automáticamente

### 3. Crear un Tablero

1. Dentro del workspace, click **"Nuevo Tablero"**
2. Ingresá:
   - **Nombre**: ej. "Sprint 1"
   - **Descripción**: opcional
   - **Color**: elegí un color de fondo
3. Guardar → se crean 3 listas automáticamente

### 4. Agregar Tareas

1. En una lista, click **"+ Nueva tarea"**
2. Completá:
   - **Título**: nombre de la tarea
   - **Descripción**: detalles (opcional)
   - **Asignado a**: elegí uno o más usuarios
   - **Prioridad**: Baja, Media, Alta, Crítica
   - **Fecha límite**: opcional
3. Guardar → aparece en la lista

### 5. Mover Tareas (Drag & Drop)

1. **Click y mantener** sobre una tarea
2. **Arrastrar** a la lista destino
3. **Soltar** → se guarda automáticamente

### 6. Marcar Tareas Completadas

1. Abrir detalle de la tarea
2. Click en **"Marcar como completada"**
3. La tarea registra fecha de completado

### 7. Modo Oscuro

1. Click en el ícono **🌙** en el navbar
2. Cambia entre modo claro y oscuro
3. Tu preferencia se guarda automáticamente

---

## 📁 Estructura del Proyecto

```
taskmaster/
│
├── apps/                          # Aplicaciones Django
│   ├── users/                     # Autenticación y usuarios
│   │   ├── models.py              # Modelo User personalizado
│   │   ├── views.py               # Vistas de registro/perfil
│   │   └── forms.py               # Formularios de usuario
│   │
│   ├── workspaces/                # Espacios de trabajo
│   │   ├── models.py              # Workspace, WorkspaceMember
│   │   └── views.py               # CRUD de workspaces
│   │
│   ├── boards/                    # Tableros y listas
│   │   ├── models.py              # Board, BoardList
│   │   └── views.py               # Gestión de tableros
│   │
│   ├── tasks/                     # Tareas
│   │   ├── models.py              # Task con prioridades
│   │   ├── views.py               # CRUD + Drag & Drop
│   │   └── forms.py               # Formularios de tareas
│   │
│   └── core/                      # Utilidades comunes
│       └── views.py               # Vista home
│
├── config/                        # Configuración Django
│   ├── settings.py                # Settings principal
│   └── urls.py                    # URLs principales
│
├── templates/                     # Templates HTML
│   ├── base.html                  # Template base
│   ├── home.html                  # Página inicial
│   ├── partials/                  # Componentes reutilizables
│   ├── users/                     # Templates de usuarios
│   ├── workspaces/                # Templates de workspaces
│   ├── boards/                    # Templates de tableros
│   └── tasks/                     # Templates de tareas
│
├── static/                        # Archivos estáticos
│   ├── css/
│   │   └── styles.css             # Estilos personalizados
│   └── js/
│       ├── board.js               # Drag & drop
│       └── darkmode.js            # Toggle modo oscuro
│
├── media/                         # Archivos subidos
│   └── avatars/                   # Avatares de usuarios
│
├── docs/                          # Documentación
│   ├── propuesta-proyecto-taskmaster.md
│   ├── sistema-gestion-tareas-avanzado.md
│   └── DRAG_DROP_FEATURE.md
│
├── manage.py                      # Script de Django
├── requirements.txt               # Dependencias Python
├── .env                           # Variables de entorno
├── .gitignore                     # Archivos ignorados por Git
├── README.md                      # Este archivo
├── CHANGELOG.md                   # Historial de versiones
├── DEVELOPMENT.md                 # Guía para desarrolladores
└── VERSION                        # Número de versión actual
```

---

## 🛠️ Tecnologías

### Backend
- **Django 6.0.3** - Framework web Python
- **Python 3.10+** - Lenguaje de programación
- **SQLite** - Base de datos (desarrollo)
- **python-decouple** - Gestión de variables de entorno

### Frontend
- **Bootstrap 5** - Framework CSS
- **Bootstrap Icons** - Iconos
- **SortableJS** - Drag & drop de tareas
- **Vanilla JavaScript** - Interactividad

### Librerías Adicionales
- **django-crispy-forms** - Renderizado de formularios
- **crispy-bootstrap5** - Integración Bootstrap
- **Pillow** - Procesamiento de imágenes
- **python-slugify** - Generación de slugs

---

## 🗺️ Roadmap

### ✅ v1.0.0 - Base del Sistema
- Autenticación de usuarios
- Workspaces y miembros
- Tableros Kanban con listas
- Tareas con prioridades y asignación
- Interfaz responsive

### ✅ v1.0.1 - Drag & Drop
- Arrastrar tareas entre listas
- Reordenar tareas
- Actualización automática

### ✅ v1.0.2 - Modo Oscuro (Actual)
- Toggle light/dark mode
- Persistencia de preferencia
- Estilos optimizados

### 🔜 v1.1 - Colaboración
- Sistema de comentarios en tareas
- Menciones de usuarios (@usuario)
- Tags/etiquetas con colores
- Búsqueda de tareas

### 🔜 v1.2 - Mejoras de Productividad
- Notificaciones in-app
- Adjuntar archivos a tareas
- Subtareas con checkboxes
- Filtros avanzados

### 🔜 v1.3 - Analytics
- Dashboard con métricas
- Gráficos de progreso
- Exportar a PDF/CSV
- Historial de actividad

### 🔜 v2.0 - API y Tiempo Real
- API REST completa
- WebSockets para notificaciones
- Integración con terceros
- Aplicación móvil

---

## 🎓 Valor Educativo

Este proyecto demuestra:

✅ Arquitectura modular de Django  
✅ Relaciones complejas entre modelos (FK, M2M)  
✅ Vistas basadas en clases (CBV)  
✅ Sistema de autenticación personalizado  
✅ Formularios y validación  
✅ AJAX y JavaScript vanilla  
✅ Responsive design con Bootstrap  
✅ Gestión de archivos estáticos y media  
✅ Buenas prácticas de desarrollo  

---

## 📝 Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

# Shell interactivo de Django
python manage.py shell

# Ejecutar tests
python manage.py test

# Recolectar archivos estáticos
python manage.py collectstatic
```

---

## 🐛 Solución de Problemas

### El servidor no inicia
```bash
# Verificar que el entorno virtual esté activo
# Windows: .\venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Verificar instalación de dependencias
pip install -r requirements.txt
```

### Error "No such table"
```bash
# Aplicar migraciones
python manage.py migrate
```

### Archivos estáticos no cargan
```bash
# Recolectar archivos estáticos
python manage.py collectstatic --noinput
```

### Olvidé mi contraseña de admin
```bash
# Crear nuevo superusuario
python manage.py createsuperuser
```

---

## 🤝 Contribuir

Este es un proyecto educativo. Sugerencias y mejoras son bienvenidas:

1. Fork el proyecto
2. Crear una rama (`git checkout -b feature/nueva-feature`)
3. Commit cambios (`git commit -m 'Agrega nueva feature'`)
4. Push a la rama (`git push origin feature/nueva-feature`)
5. Abrir Pull Request

---

## 📄 Licencia

Proyecto educativo - Libre para uso académico y aprendizaje

---

## 👥 Autores

**Proyecto TaskMaster**  
Desarrollo: Marzo 2026  
Materia: Programación / Ingeniería de Software  

---

## 🌟 ¿Te gusta el proyecto?

Si te resultó útil:
- ⭐ Dale una estrella al repositorio
- 📢 Compartí con tu equipo
- 🐛 Reportá bugs o sugerencias en Issues

---

## 📚 Recursos Adicionales

- [Documentación de Django](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [SortableJS](https://sortablejs.github.io/Sortable/)
- [DEVELOPMENT.md](DEVELOPMENT.md) - Guía para desarrolladores
- [CHANGELOG.md](CHANGELOG.md) - Historial de versiones

---

**¡Gracias por usar TaskMaster!** 🚀
