import tkinter as tk
from tkinter import ttk
import json

class GUI_load_JSON:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Journal CMS")
        self.root.geometry("1000x700")

        self.text = tk.Text(self.root)
        self.text.pack()

        # Sample JSON
        json_val = json.loads('{"a": 5, "b": 7}')

        for k in json_val:
            self.text.insert(tk.END, '{} = {}\n'.format(k, json_val[k]))
        self.text.config(state=tk.DISABLED)
