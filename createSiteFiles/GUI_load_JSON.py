import tkinter as tk
from tkinter import ttk
import json

class Home(tk.Frame):
    
    # TO DO - Any time we navigate to this page the json file should be re-read!!

    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.text = tk.Text(self)
        self.text.pack()

        with open('server\\userFiles\\user.json', 'r') as f:
            data = json.load(f)

            username = data["userName"]
            siteTitle = data["title"]
            journalTitle = data["journalTitle"]
            footer = data["footerDescription"]

            bookEntry = data["bookEntries"][0]
            date = bookEntry["date"]
            title = bookEntry["title"]
            author = bookEntry["author"]
            coverImg = bookEntry["coverURL"]
            rating = bookEntry["rating"]
            description = bookEntry["description"]
            spoilers = bookEntry["spoilers"]

            self.text.insert(tk.END, f"{username}'s {siteTitle}\n\n")
            self.text.insert(tk.END, f"{journalTitle}\n\n")
            self.text.insert(tk.END, "Latest Book Entry:\n")
            self.text.insert(tk.END, f"{date}\n {title}\n {author}\n {coverImg}\n {rating}\n {description}\n {spoilers}\n\n")
            self.text.insert(tk.END, f"{footer}\n\n")

        button1 = ttk.Button(self, text="Edit Page", command=lambda: controller.show_frame("EditPageUI"))
        button1.pack()

        self.text.config(state=tk.DISABLED)