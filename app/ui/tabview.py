
import customtkinter as ctk
from .stats_screen import StatsScreen

class TabView(ctk.CTkTabview):
    """
    An instance of customtkinter.CTkTabView, which handle all the screens of the app
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.stats_tab = self.add("Stats")
        self.stats_screen = StatsScreen(self.stats_tab)
        self.stats_tab.configure(fg_color="blue")
        self.stats_tab.rowconfigure(0, weight=1)
        self.stats_tab.columnconfigure(0, weight=1)
        self.stats_screen.grid(sticky="nsew")


