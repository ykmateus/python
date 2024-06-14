// script.js
document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        addTask(taskInput.value);
        taskInput.value = '';
    });

    taskList.addEventListener('click', (e) => {
        if (e.target.classList.contains('delete-btn')) {
            deleteTask(e.target.parentElement);
        } else if (e.target.classList.contains('edit-btn')) {
            editTask(e.target.parentElement);
        }
    });

    function addTask(taskText) {
        const li = document.createElement('li');
        li.textContent = taskText;
        const editButton = document.createElement('button');
        editButton.textContent = 'Editar';
        editButton.classList.add('edit-btn');
        li.appendChild(editButton);
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Excluir';
        deleteButton.classList.add('delete-btn');
        li.appendChild(deleteButton);
        taskList.appendChild(li);
    }

    function deleteTask(taskItem) {
        taskList.removeChild(taskItem);
    }

    function editTask(taskItem) {
        const newTaskText = prompt('Editar tarefa:', taskItem.firstChild.textContent);
        if (newTaskText) {
            taskItem.firstChild.textContent = newTaskText;
        }
    }
});
