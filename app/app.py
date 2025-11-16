
import os
from app.ui.main_window import MainWindow
from app.src.tasks.tasks_data_handler import tasks_data_handler
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
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data_handler.load_tasks_data()
        self.main_window = MainWindow(self, self.user)


    def running(self):
        self.auto_save()
        self.logger.info("Main window drawed")
        self.main_window.mainloop()
        self.exit_app()

    def exit_app(self):
        self.logger.info("Saving data...")
        self.tasks_data_handler.save_tasks_data()
        self.logger.info("Exit folowing main window closure")
        exit()

    def auto_save(self):
        self.logger.info("Auto saving...")
        self.tasks_data_handler.save_tasks_data()
        self.main_window.after(120000, self.auto_save)

