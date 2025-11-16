
import os

base_path = os.path.join(os.getenv("APPDATA", os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Tasky")), "Tasky")
data_dir = os.path.join(base_path, "data") # Data folder

user_data_dir = os.path.join(data_dir, "user") # User data directory
tasks_backup_file = os.path.join(user_data_dir, "tasks.json") # Tasks backup file 

logs_dir = os.path.join(base_path, "logs")
logs_basefile = os.path.join(logs_dir, "app.log")