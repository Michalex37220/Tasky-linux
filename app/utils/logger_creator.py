
import logging

def create_logger(name: str, level: int=3):
    logger = logging.getLogger(name)
    logger.setLevel(level)
