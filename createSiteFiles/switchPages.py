import tkinter as tk
from tkinter import ttk
from GUI_load_JSON import Home
from createPageUI import EditPageUI

class tkinterApp(tk.Frame):
    def __init__(self, root, *args, **kwargs): 
        super().__init__(root, *args, **kwargs)
        self.pack(fill="both", expand=True)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, EditPageUI):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# app = tkinterApp()
# app.mainloop()