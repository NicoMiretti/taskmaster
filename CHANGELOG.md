# TaskMaster - Changelog

## Version 1.0.2 (Marzo 2026)

### Nueva Funcionalidad
- ✅ **Modo Oscuro** - Toggle para cambiar entre tema claro y oscuro
  - Botón en el navbar con ícono de luna/sol
  - Preferencia guardada en localStorage
  - Transiciones suaves entre temas
  - Estilos optimizados para ambos modos
  - Funciona en todas las páginas

### Archivos Agregados
- `static/js/darkmode.js` - Lógica del toggle y persistencia

### Archivos Modificados
- `static/css/styles.css` - Estilos para dark mode
- `templates/partials/navbar.html` - Botón de toggle
- `templates/base.html` - Carga del script darkmode.js

---

## Version 1.0.1 (Marzo 2026)

### Nueva Funcionalidad
- ✅ **Drag & Drop de tareas** - Ahora podés arrastrar tareas entre listas
  - Arrastrar tareas de una lista a otra
  - Reordenar tareas dentro de la misma lista
  - Actualización automática en base de datos
  - Feedback visual durante el arrastre
  - Actualización de contadores en tiempo real

### Archivos Agregados
- `static/js/board.js` - Lógica de drag & drop con SortableJS
- `docs/DRAG_DROP_FEATURE.md` - Documentación de la funcionalidad

### Archivos Modificados
- `apps/tasks/views.py` - Nueva vista `TaskMoveView`
- `apps/tasks/urls.py` - Nueva ruta para mover tareas
- `static/css/styles.css` - Estilos para drag & drop
- `templates/boards/board_detail.html` - Integración de SortableJS

---

## Version 1.0.0 (Marzo 2026)

### Features Implementadas

#### Core Functionality
- ✅ Sistema de autenticación completo (login, registro, logout)
- ✅ Modelo de usuario personalizado con avatar y biografía
- ✅ Arquitectura modular con apps separadas

#### Workspaces
- ✅ Crear y gestionar workspaces
- ✅ Sistema de miembros con roles (owner, admin, member, viewer)
- ✅ Listar workspaces por usuario

#### Boards (Tableros)
- ✅ Crear tableros dentro de workspaces
- ✅ Listas personalizables (columnas Kanban)
- ✅ Color de fondo personalizable
- ✅ Creación automática de listas por defecto

#### Tasks (Tareas)
- ✅ Crear, editar y eliminar tareas
- ✅ Asignar múltiples usuarios a una tarea
- ✅ Sistema de prioridades (baja, media, alta, crítica)
- ✅ Fechas límite
- ✅ Marcar tareas como completadas
- ✅ Vista detallada de cada tarea

#### UI/UX
- ✅ Interfaz responsive con Bootstrap 5
- ✅ Diseño estilo Kanban board
- ✅ Iconos con Bootstrap Icons
- ✅ Mensajes de feedback
- ✅ Navegación intuitiva

### Arquitectura
- Base de datos SQLite (desarrollo)
- Estructura modular y escalable
- Modelos preparados para features futuras
- Settings configurables con decouple

### Próximas Versiones

#### v1.1 (Planificado)
- Sistema de comentarios en tareas
- Tags/etiquetas con colores
- Búsqueda básica de tareas
- Filtros por prioridad y asignado

#### v1.2 (Planificado)
- Notificaciones in-app
- Adjuntar archivos a tareas
- Subtareas con checkboxes
- Historial de actividad

#### v2.0 (Futuro)
- API REST con Django REST Framework
- WebSockets para notificaciones en tiempo real
- Drag & drop de tareas entre listas
- Analytics y reportes
- Exportar datos a PDF/CSV
