// Drag and Drop functionality for TaskMaster
document.addEventListener('DOMContentLoaded', function() {
    const lists = document.querySelectorAll('.task-list');
    
    if (lists.length === 0) return; // No lists on this page
    
    lists.forEach(list => {
        new Sortable(list, {
            group: 'shared',
            animation: 150,
            ghostClass: 'task-ghost',
            dragClass: 'task-dragging',
            handle: '.task-card',
            
            onEnd: function(evt) {
                const taskId = evt.item.dataset.taskId;
                const newListId = evt.to.dataset.listId;
                const newPosition = evt.newIndex;
                
                // Show loading state
                evt.item.style.opacity = '0.5';
                
                // Send AJAX request to update task
                fetch(`/tasks/${taskId}/move/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `list_id=${newListId}&position=${newPosition}`
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Remove opacity
                        evt.item.style.opacity = '1';
                        
                        // Update counters
                        updateListCounters();
                    } else {
                        // Revert the move
                        alert('Error al mover la tarea: ' + (data.error || 'Error desconocido'));
                        location.reload();
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error de conexión. Recargando página...');
                    location.reload();
                });
            }
        });
    });
    
    function updateListCounters() {
        document.querySelectorAll('.task-list').forEach(list => {
            const count = list.querySelectorAll('.task-card').length;
            const counter = list.closest('.board-list').querySelector('.task-count');
            if (counter) {
                counter.textContent = count;
            }
        });
    }
});
