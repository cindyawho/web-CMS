import tkinter as tk
from tkinter import ttk
import json
import os
from pathlib import Path

class Home(tk.Frame):
    # print("Current directory:", os.getcwd()) in case debugging is needed
    jsonFilePath = Path('server/user.json')

    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.text = tk.Text(self)
        self.text.pack()

        if os.path.exists(self.jsonFilePath):
            with open(self.jsonFilePath, 'r') as f:
                data = json.load(f)
                # print(data)

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
        else:
            print(f"Error: file {self.jsonFilePath} not found!\n")

        button1 = ttk.Button(self, text="Edit Page", command=lambda: controller.show_frame("EditPageUI"))
        button1.pack()

        self.text.config(state=tk.DISABLED)

    def refresh(self):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)  # Clear the existing content

        if os.path.exists(self.jsonFilePath):
            with open(self.jsonFilePath, 'r') as f:
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
                self.text.insert(tk.END, f" Date:\t\t{date}\n Title:\t\t{title}\n Author:\t\t{author}\n Cover Image URL:\t\t{coverImg}\n Rating:\t\t{rating}\n Review:\t\t{description}\n Spoilers:\t\t{spoilers}\n\n")
                self.text.insert(tk.END, f"Footer:\n{footer}\n\n")
        else:
            self.text.insert(tk.END, f"Error: file {self.jsonFilePath} not found!\n")

        self.text.config(state=tk.DISABLED)
