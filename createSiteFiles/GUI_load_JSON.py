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
        with open('createSiteFiles\\userFiles\\user.json', 'r') as f:
            data = json.load(f)
            # print(data)
            username = data["userName"]
            siteTitle = data["title"]
            journalTitle = data["journalTitle"]
            footer = data["footerDescription"]

            bookEntry = data["bookEntries"][0]
            date = bookEntry["date"]
            title = bookEntry["title"]
            author = bookEntry["date"]
            coverImg = bookEntry["coverURL"]
            rating = bookEntry["rating"]
            description = bookEntry["description"]
            spoilers = bookEntry["spoilers"]

            self.text.insert(tk.END, f"{username}'s {siteTitle}\n\n")
            self.text.insert(tk.END, f"{journalTitle}\n\n")
            self.text.insert(tk.END, f"{date}\n {title}\n {author}\n {coverImg}\n {rating}\n {description}\n {spoilers}\n")
            self.text.insert(tk.END, f"{footer}\n\n")
        self.text.config(state=tk.DISABLED)
