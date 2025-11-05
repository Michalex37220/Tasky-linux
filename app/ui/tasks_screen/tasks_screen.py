import customtkinter as ctk
from .all_tasks_fr import AllTasksFrame
from .task_editor_fr import TaskEditorFrame
from ...src.tasks.tasks_data_handler import tasks_data_handler

class TasksScreen(ctk.CTkFrame):

    def __init__(self, master, user, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data = self.tasks_data_handler.tasks_data

        self.task_editor_fr = TaskEditorFrame(self, user)
        self.task_editor_fr.grid(row=0, sticky="nse")

        self.all_tasks_fr = AllTasksFrame(self, user)
        self.all_tasks_fr.grid(row=0, sticky="nsw")
        