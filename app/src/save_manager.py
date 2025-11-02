
from ..libs import path_maker
from .tasks.tasks_data_handler import tasks_data_handler
import json

def open_file(base_path: str, relative_path: str, mode: str):
    filepath = path_maker.make_path(base_path, relative_path)

    if filepath:

        with open(path_maker.make_path(base_path, relative_path), mode) as f:
            return f
        
    else:
        return
    
def save_tasks_data(base_path, relative_path):
    file = open_file(base_path, relative_path, mode="w")

    if file:
        json.dump(tasks_data_handler.tasks_data, file)
    


