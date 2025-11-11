
import os
import logging
import logging.handlers
from typing import Literal
from app.utils import paths

paths_alias = {
    "data_dir":paths.data_dir,
    "logs_dir":paths.logs_dir,
    "user_data_dir":paths.user_data_dir
}

def check_and_make(*paths_alias):
    """
    Check the existence of a path alias in the path database of the program. Create it if the path is found in the database, but don't exists

    Args:
        - path_name (str): a alias of a path. See the attribute 'paths_list' for see paths alias

    """

    for alias in paths_alias:
        if not alias in paths_alias:
            raise ValueError(f"No path found for given alias '{alias}'")

        else:
            path = paths_alias[alias]

        if not os.path.exists(path):
            print(f"[Info] Folder at {path} not found, attempting to make it...")

            try:
                os.mkdir(path)

            except Exception as e:
                print(f"[Error] Failed to create folder at {path}: {e}")

            else:
                print(f"[Info] Folder {path} created")

