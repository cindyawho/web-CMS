import switchPages
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Book Journal CMS")
    root.geometry("1200x900")
    
    app = switchPages.tkinterApp(root)
    root.mainloop()