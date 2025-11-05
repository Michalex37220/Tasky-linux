
from ...ui.tasks_screen.task_fr import TaskFrame

def create_task(master, user, task_data):
    return TaskFrame(master, task_data=task_data, user=user)
