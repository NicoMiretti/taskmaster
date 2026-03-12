# TaskMaster - Drag & Drop Feature

## ✅ Funcionalidad Implementada

Se agregó la capacidad de **arrastrar y soltar tareas** entre listas en el tablero Kanban.

### Características

- ✅ Arrastrar tareas entre listas (ej: "Por Hacer" → "En Progreso")
- ✅ Reordenar tareas dentro de la misma lista
- ✅ Actualización automática en la base de datos
- ✅ Feedback visual durante el arrastre
- ✅ Actualización de contadores en tiempo real
- ✅ Manejo de errores con recarga automática

### Archivos Modificados/Creados

1. **`apps/tasks/views.py`**
   - Agregada clase `TaskMoveView` para manejar el movimiento de tareas
   - Endpoint POST que actualiza lista y posición
   - Reordenamiento automático de posiciones

2. **`apps/tasks/urls.py`**
   - Nueva ruta: `/tasks/<id>/move/`

3. **`static/js/board.js`** (NUEVO)
   - Implementación de SortableJS
   - Lógica de drag & drop
   - Llamada AJAX al backend
   - Actualización de contadores

4. **`static/css/styles.css`**
   - Estilos para `.task-card` con cursor grab/grabbing
   - Clases `.task-ghost` y `.task-dragging` para feedback visual
   - Altura mínima para `.task-list`

5. **`templates/boards/board_detail.html`**
   - Agregados `data-task-id` y `data-list-id` en elementos
   - Contenedor `.task-list` para SortableJS
   - Carga de SortableJS CDN
   - Carga de board.js

### Cómo Funciona

1. **Usuario arrastra una tarea** de una lista a otra
2. **SortableJS detecta el evento** `onEnd`
3. **JavaScript envía petición POST** a `/tasks/{id}/move/`
   - Parámetros: `list_id`, `position`
4. **Backend actualiza** la tarea en la BD
5. **Backend reordena** todas las tareas de ambas listas
6. **Frontend actualiza** los contadores de tareas

### Seguridad

- ✅ Verificación de permisos (usuario debe ser miembro del workspace)
- ✅ Validación de lista destino
- ✅ Manejo de excepciones
- ✅ CSRF exempt (necesario para AJAX simple)

### Uso

1. **Acceder a un tablero** con tareas
2. **Click y mantener** sobre una tarea
3. **Arrastrar** a la lista deseada
4. **Soltar** - la tarea se guarda automáticamente

### Mejoras Futuras (v1.2)

- [ ] Animaciones más suaves
- [ ] Confirmación opcional antes de mover
- [ ] Deshacer último movimiento
- [ ] Historial de movimientos
- [ ] Notificar a usuarios asignados cuando se mueve su tarea

### Testing

Para probar:
```bash
1. Crear un workspace
2. Crear un tablero
3. Crear varias tareas en diferentes listas
4. Arrastrar tareas entre listas
5. Verificar que se guardan correctamente (recargar página)
```

## Tecnología Utilizada

- **SortableJS**: Librería JavaScript para drag & drop (https://sortablejs.github.io/Sortable/)
- **Fetch API**: Para peticiones AJAX
- **Django CSRF exempt**: Para simplificar AJAX (en producción considerar usar tokens)

## Versión

Feature agregada en: **v1.0.1**
