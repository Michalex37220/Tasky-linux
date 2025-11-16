
import os
from app.ui.main_window import MainWindow
from app.src.user import User
from app.src  import save_manager
import logging, logging.handlers
from app.src.boot import check_and_make 
from app.utils import paths

class App:

    def __init__(self):
        self.user = User(self)
        check_and_make("program_dir", "data_dir", "user_data_dir", "logs_dir")
        self.logger = logging.getLogger(__name__)
        self.main_window = MainWindow(self, self.user)


    def running(self):
        self.main_window.mainloop()
        self.exit_app()

    def exit_app(self):
        self.logger.info("Saving data...")
        self.main_window.tasks_data_handler.save_tasks_data()

    def auto_save(self):
        self.main_window.tasks_data_handler.save_tasks_data()
        self.main_window.after(300000, self.auto_save)

