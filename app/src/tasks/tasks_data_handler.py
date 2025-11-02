
from tkinter.messagebox import showerror, askretrycancel
import json
from ...libs import path_maker

class TasksDataHandler():

    def __init__(self, tasks_data: list=[]):
        self.tasks_data = tasks_data
        self.relative_backup_path =  "../../data/user/tasks_data_backup.json"
        self.base_path = __file__

    def save_tasks_data(self, **kwargs):
        self.relative_backup_path = kwargs.get("relative_path", self.relative_backup_path)
        self.base_path = kwargs.get("base_path", self.base_path)
        file = path_maker.make_path(self.base_path, self.relative_backup_path, check_existence=False)

        with open(file, "w") as f:
            json.dump(self.tasks_data, f)

    def load_tasks_data(self, **kwargs):
        self.relative_backup_path = kwargs.get("relative_path", self.relative_backup_path)
        self.base_path = kwargs.get("base_path", self.base_path)
        file = path_maker.make_path(self.base_path, self.relative_backup_path, check_existence=False)

        try:
            
            with open(file, "r") as f:
                self.tasks_data = json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            showerror(title="Tasks Gamifier | Load Data", message="Sorry, but the program could not load the saved data.")
            return
        
tasks_data_handler = TasksDataHandler()