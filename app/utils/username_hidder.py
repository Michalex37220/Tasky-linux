
import os

def remove_username(path: str):
    username = os.path.expanduser("~")
    path = path.replace(username, "~")
    return path