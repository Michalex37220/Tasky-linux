
import json
from ...src.save_manager import save_data, load_data
from app.utils import paths
import os

class TasksDataHandler():

    def __init__(self, tasks_data: list=[]):
        self.tasks_data = tasks_data
        self.tasks_backup_filepath = paths.tasks_backup_file

    def save_tasks_data(self):
        save_data(self.tasks_backup_filepath, self.tasks_data)
       

    def load_tasks_data(self):
        self.tasks_data = load_data(self.tasks_backup_filepath)

        if not self.tasks_data:
            self.tasks_data = []

        
tasks_data_handler = TasksDataHandler()

