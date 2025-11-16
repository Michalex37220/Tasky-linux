
import logging
import logging.handlers
from app.utils import paths

logger = logging.getLogger()
logs_handler = logging.handlers.RotatingFileHandler(paths.logs_basefile, maxBytes=100000, backupCount=3)
logs_handler.setLevel("DEBUG")
logs_formatter = logging.Formatter(fmt="[{asctime}] - [{name}] - [{levelname}] : {msg}", style="{")
logs_handler.setFormatter(logs_formatter)
logger.addHandler(logs_handler)
logger.setLevel("DEBUG")