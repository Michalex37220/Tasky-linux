import logging 
import customtkinter as ctk
from .tabview import TabView

class App(ctk.CTk):
    """
    The windows

    Inherit from customtkinter.CTk
    """

    def __init__(self):
        super().__init__()
        self.title("Tasks Gamifier")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.tabview = TabView(self)
        self.tabview.grid(sticky="nsew")

