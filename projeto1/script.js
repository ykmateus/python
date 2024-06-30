document.getElementById('addTaskButton').addEventListener('click', addTask);

function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();

    if (taskText === '') {
        return;
    }

    const taskItem = document.createElement('li');
    taskItem.classList.add('task-item');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', toggleTaskCompletion);

    const taskSpan = document.createElement('span');
    taskSpan.textContent = taskText;

    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remover';
    removeButton.classList.add('remove');
    removeButton.addEventListener('click', removeTask);

    taskItem.appendChild(checkbox);
    taskItem.appendChild(taskSpan);
    taskItem.appendChild(removeButton);

    document.getElementById('taskList').appendChild(taskItem);

    taskInput.value = '';
}

function removeTask(event) {
    const taskItem = event.target.parentElement;
    taskItem.remove();
}

function toggleTaskCompletion(event) {
    const taskItem = event.target.parentElement;
    if (event.target.checked) {
        taskItem.classList.add('completed');
    } else {
        taskItem.classList.remove('completed');
    }
}
