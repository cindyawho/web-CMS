import createPageUI as cui
import GUI_load_JSON as loadJSON
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = loadJSON.CreatePage(root)
    root.mainloop()