
import tkinter as tk
import logging
from app.app import App

logger = logging.getLogger("app")
app = App()
print("Welcome to Tasks Manager v0.1.0")
logger.info("Init app...")
app.running()

