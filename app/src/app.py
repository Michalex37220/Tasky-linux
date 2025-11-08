
import os
from ..ui.main_window import MainWindow
from app.src.user import User
from app.src  import save_manager

class App:

    def __init__(self):
        self.user = User(self)
        self.base_path =  os.path.join(os.getenv("APPDATA", os.path.join(os.path.expanduser("~"), "AppData\\Roaming\\Tasks Manager")), "Tasks Manager")
        self.datadir_path = os.path.join(self.base_path, "data")
        self.logs_dir_path = os.path.join(self.base_path, "logs")

        if not os.path.exists(self.base_path):
            print("No backup folder found !")
            print("Creating backup folder...")
            os.mkdir(self.base_path)
            os.mkdir(self.datadir_path)
            os.mkdir(self.logs_dir_path)

        self.backupfilename = "tasks.json"
        self.backupfile_path = os.path.join(self.base_path, self.backupfilename)
        self.main_window = MainWindow(self, self.user)

    def running(self):
        self.main_window.mainloop()
        self.exit_app()

    def exit_app(self):
        print("Saving data...")
        self.main_window.tasks_data_handler.save_tasks_data()
        print("Closing main window...")

    def auto_save(self):
        print("Saving data...")
        self.main_window.tasks_data_handler.save_tasks_data()
        self.main_window.after(300000, self.auto_save)

    def boot(self):
        self.first_boot = True
