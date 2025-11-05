
import json
from tkinter.messagebox import showerror
import os
from tkinter.messagebox import showinfo
from .save_manager import save_data, load_data

class User:

    def __init__(self, master, **kwargs) -> None:
        self.master = master
        self.dev_mode =  True
        self.completed_tasks = []
