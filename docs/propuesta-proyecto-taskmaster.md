# Propuesta de Proyecto: TaskMaster
### Sistema de Gestión de Tareas Colaborativo

**Integrantes:** [Nombre 1], [Nombre 2], [Nombre 3] | **Materia:** [Nombre] | **Fecha:** Marzo 2026

---

## 📱 Idea de Producto Digital

**TaskMaster** es una plataforma web de gestión de tareas colaborativa tipo Kanban, diseñada para equipos estudiantiles y pequeños grupos de trabajo. Permite crear tableros compartidos, asignar tareas con responsables y fechas límite, comentar, y hacer seguimiento visual del progreso del proyecto. Combina la simplicidad de una pizarra física con las ventajas digitales: acceso remoto, notificaciones, historial y búsqueda.

## 💎 Propuesta de Valor

**Problema:** La desorganización en proyectos colaborativos genera pérdida de información en chats, duplicación de trabajo, falta de visibilidad sobre el progreso e incumplimiento de plazos.

**Solución:** TaskMaster centraliza toda la información en tableros visuales, mostrando de un vistazo quién hace qué, qué está bloqueado y qué está completo. Notificaciones inteligentes mantienen al equipo sincronizado sin necesidad de reuniones constantes.

**Diferenciadores:** Gratuito para estudiantes, interfaz simple sin curva de aprendizaje, enfocado en equipos pequeños (no empresas), código abierto.

---

## 🏆 Competidores

### Online: Trello
**Fortalezas:** Interfaz intuitiva, gran adopción, integraciones múltiples, versión gratuita.  
**Debilidades:** Funcionalidades avanzadas solo en planes premium, puede ser lento con muchos datos.  
**Oportunidad:** Ofrecer features avanzadas gratis, orientado específicamente a educación.

### Offline: Pizarra con Post-its
**Fortalezas:** Visual, flexible, tangible, cero tecnología requerida.  
**Debilidades:** Solo presencial, sin historial, vulnerable a pérdidas, imposible colaborar remotamente.  
**Oportunidad:** Replicar la simplicidad visual pero con acceso remoto, historial permanente y colaboración asíncrona.

---

## 👤 Usuario Principal

**María, 22 años - Líder de Equipo Universitario**
- Estudiante de Ingeniería en Sistemas, coordina equipo de 4 personas en proyecto final
- Maneja clases, trabajo part-time y el proyecto grupal simultáneamente
- Frustración actual: coordinar por WhatsApp genera caos, mensajes perdidos, no sabe el progreso sin preguntar constantemente
- Necesita: visibilidad del estado del proyecto, asignar tareas claras, recibir notificaciones de cambios importantes, acceder desde cualquier dispositivo

---

## 📖 Escenario de Uso: Proyecto Final de Ingeniería

**Contexto:** María y su equipo tienen 6 semanas para entregar proyecto completo (backend, frontend, BD, docs). En proyectos anteriores coordinaba por WhatsApp: tareas perdidas entre memes, trabajo duplicado, sorpresas de último momento.

**Con TaskMaster:**

1. **Setup (15 min):** María crea workspace "Proyecto Final", invita compañeros, crea tablero con listas: "Por Hacer", "En Progreso", "En Revisión", "Completado"

2. **Planificación (30 min reunión):** Crean tareas asignadas:
   - "Diseñar BD" → Juan | "Desarrollar API" → Pedro | "Interfaz login" → Ana | "Documentación" → María
   - Cada una con fecha límite, prioridad y etiquetas (Backend/Frontend/Docs)

3. **Trabajo asíncrono (durante la semana):**
   - Juan termina BD, mueve tarea a "Completado", comenta: "@Pedro ya está lista"
   - Pedro recibe notificación, descarga diagrama adjunto, empieza API
   - Ana sube screenshot, pregunta: "@María ¿te gusta este diseño?"
   - María revisa desde el celular: todo progresa bien

4. **Seguimiento (viernes):** Reunión virtual, ven tablero: 4 completadas, 3 en progreso, 2 bloqueadas. María identifica cuello de botella (falta definir autenticación), crean tarea nueva con prioridad ALTA, ajustan fechas.

**Resultados:** Sin confusión, sin duplicación, visibilidad constante, historial completo, entrega exitosa a tiempo.

---

## 🎯 Conclusión

TaskMaster resuelve un problema real de desorganización en equipos colaborativos, combinando simplicidad visual con ventajas digitales. Técnicamente viable con Django, representa un desafío académico adecuado y útil para la realidad de los estudiantes.
