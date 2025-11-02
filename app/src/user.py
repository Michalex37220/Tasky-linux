
import json
from tkinter.messagebox import showerror
from ..libs import path_maker

class User:

    def __init__(self, name: str="Player", current_xp: int=0, level: int=0) -> None:
        self.name = name
        self.level = level
        self.current_xp = current_xp
        self.base_path = __file__
        self.relative_backup_path = "../data/user/player_stats_backup.json"

    def save_data(self, **kwargs):
        self.relative_backup_path = kwargs.get("relative_path", self.relative_backup_path)
        self.base_path = kwargs.get("base_path", self.base_path)
        file = path_maker.make_path(self.base_path, self.relative_backup_path, check_existence=False)

        with open(file, "w") as f:
            json.dump(self.tasks_data, f)

    def load_data(self, **kwargs):
        self.relative_backup_path = kwargs.get("relative_path", self.relative_backup_path)
        self.base_path = kwargs.get("base_path", self.base_path)
        file = path_maker.make_path(self.base_path, self.relative_backup_path, check_existence=False)

        try:
            
            with open(file, "r") as f:
                self.tasks_data = json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            showerror(title="Tasks Gamifier | Load Data", message="Sorry, but the program could not load the saved data.")
            return

user = User()