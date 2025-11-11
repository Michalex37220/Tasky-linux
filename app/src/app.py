
import os
from ..ui.main_window import MainWindow
from app.src.user import User
from app.src  import save_manager
from app.src import boot_mgr

class App:

    def __init__(self):
        self.user = User(self)
        self.boot_mgr = boot_mgr.BootManager()
        self.boot_mgr.check_and_make("program_dir", "data_dir", "user_data_dir", "logs_dir")
        self.check_and_make_finished = True

        if self.check_and_make_finished:
            self.logger = self.boot_mgr.create_logger("app")
            self.main_window = MainWindow(self, self.user)


    def running(self):
        self.main_window.mainloop()
        self.exit_app()

    def exit_app(self):
        self.logger.info("Saving data...")
        self.main_window.tasks_data_handler.save_tasks_data()
        print("Closing main window...")

    def auto_save(self):
        print("Saving data...")
        self.main_window.tasks_data_handler.save_tasks_data()
        self.main_window.after(300000, self.auto_save)

    def boot(self):
        self.first_boot = True
