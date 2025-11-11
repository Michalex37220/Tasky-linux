
import os
import logging
import logging.handlers
from typing import Literal
from app.utils import paths

class BootManager:

    def __init__(self):
        self.first_boot = False
        self.paths_list = {
            "data_dir":paths.data_dir,
            "user_data_dir":paths.user_data_dir,
            "program_dir":paths.base_path,
            'logs_dir':paths.logs_dir
        }
        self.logger_finised = False
        self.check_and_make_finished = False

    def check_and_make(self, *paths_alias):
        """
        Check the existence of a path alias in the path database of the program. Create it if the path is found in the database, but don't exists

        Args:
            - path_name (str): a alias of a path. See the attribute 'paths_list' for see paths alias

        """

        for alias in paths_alias:
            if not alias in self.paths_list:
                raise ValueError(f"No path found for given alias '{alias}'")

            else:
                path = self.paths_list[alias]

            if not os.path.exists(path):
                self.first_boot = True
                print(f"[Info] Folder at {path} not found, attempting to make it...")

                try:
                    os.mkdir(path)

                except Exception as e:
                    print(f"[Error] Failed to create folder at {path}: {e}")

                else:
                    print(f"[Info] Folder {path} created")

    def create_logger(self, name: str, **kwargs):

        logger = logging.getLogger(name)
        log_handler = logging.handlers.RotatingFileHandler(paths.logs_basefile, backupCount=3, maxBytes=1000000)
        log_formatter = logging.Formatter("{asctime} - {name} - [{levelname}]: {message}", style="{")
        log_handler.setFormatter(log_formatter)
        logger.addHandler(log_handler)
        logger.setLevel(5)

        return logger

    