import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from writeHTML import *
from writeCSS import *
from writeJSONfile import *

class EditPageUI(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Styling
        style = ttk.Style()
        style.configure("title.TLabel", foreground="black", padding=10, font=('Courier New', 14))
        style.configure("text.TLabel", foreground="black", padding=10,  font=('Arial', 14), anchor="e", width=20)
        style.configure("TEntry", foreground = "blue")

        # Grab existing json data ~~~~~~~~~~~~~~~~~~~~~~~
        self.data = self.readFile()
        username = self.data["userName"]
        siteTitle = self.data["title"]
        journalTitle = self.data["journalTitle"]
        footer = self.data["footerDescription"]
        bookEntry = self.data["bookEntries"][0]
        date = bookEntry["date"]
        title = bookEntry["title"]
        author = bookEntry["author"]
        coverImg = bookEntry["coverURL"]
        rating = bookEntry["rating"]
        description = bookEntry["description"]
        spoilers = bookEntry["spoilers"]

        # HTML Title
        self.greetLabel = ttk.Label(self, text="Welcome to your Book Journal Content Management System", style="title.TLabel")
        self.greetLabel.grid(row=0, column=0, columnspan=4, pady=20, padx=20)

        # User Inputs for HTML Page
        # Row 1 Username and site title
        self.nameLabel = ttk.Label(self, text="Display Name: ", style="text.TLabel")
        self.nameLabel.grid(row=1, column=0, sticky='e', padx=10, pady=5)
        self.nameEntry = ttk.Entry(self, style="TEntry", width=30)
        self.nameEntry.insert(tk.END, username)
        self.nameEntry.grid(row=1, column=1, sticky='w', padx=5)

        self.siteTitleLabel = ttk.Label(self, text="Site Heading: ", style="text.TLabel")
        self.siteTitleLabel.grid(row=1, column=2, sticky='e', padx=10, pady=5)
        self.siteTitleEntry = ttk.Entry(self, style="TEntry", width=30)
        self.siteTitleEntry.insert(tk.END, siteTitle)
        self.siteTitleEntry.grid(row=1, column=3, sticky='w', padx=5)

        # Row 2 Book title and author
        self.bookTitleLabel = ttk.Label(self, text="Book Title: ", style="text.TLabel")
        self.bookTitleLabel.grid(row=2, column=0, sticky='e', padx=10, pady=5)
        self.bookTitleEntry = ttk.Entry(self, style="TEntry", width=30)
        self.bookTitleEntry.insert(tk.END, title)
        self.bookTitleEntry.grid(row=2, column=1, sticky='w', padx=5)

        self.authorLabel = ttk.Label(self, text="Author: ", style="text.TLabel")
        self.authorLabel.grid(row=2, column=2, sticky='e', padx=10, pady=5)
        self.authorEntry = ttk.Entry(self, style="TEntry", width=30)
        self.authorEntry.insert(tk.END, author)
        self.authorEntry.grid(row=2, column=3, sticky='w', padx=5)

        # Row 3 date read and rating
        self.dateLabel = ttk.Label(self, text="Date Finished: ", style="text.TLabel")
        self.dateLabel.grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.dateEntry = ttk.Entry(self, style="TEntry", width=30)
        self.dateEntry.insert(tk.END, date)
        self.dateEntry.grid(row=3, column=1, sticky='w', padx=5)

        self.ratingLabel = ttk.Label(self, text="Rating: ", style="text.TLabel")
        self.ratingLabel.grid(row=3, column=2, sticky='e', padx=10, pady=5)
        self.ratingEntry = ttk.Entry(self, style="TEntry", width=30)
        self.ratingEntry.insert(tk.END, rating)
        self.ratingEntry.grid(row=3, column=3, sticky='w', padx=5)

        # Row 4 Description and cover img
        self.descLabel = ttk.Label(self, text="Review: ", style="text.TLabel")
        self.descLabel.grid(row=4, column=0, sticky='e', padx=10, pady=5)
        self.descEntry = tk.Text(self, width=40, height=7)
        self.descEntry.insert(tk.END, description)
        self.descEntry.grid(row=4, column=1, sticky='w', padx=5)

        self.imgLabel = ttk.Label(self, text="Image URL: ", style="text.TLabel")
        self.imgLabel.grid(row=4, column=2, sticky='e', padx=10, pady=5)
        self.imgEntry = ttk.Entry(self, style="TEntry", width=30)
        self.imgEntry.insert(tk.END, coverImg)
        self.imgEntry.grid(row=4, column=3, sticky='w', padx=5)

         # CSS Title
        self.CSSgreetLabel = ttk.Label(self, text="Time to Style Your Site! If nothing is selected, default styling will be used.", style="title.TLabel")
        self.CSSgreetLabel.grid(row=5, column=0, columnspan=10, pady=(35, 20), padx=20)
        
        # User Inputs for CSS
        self.bgColorVar = tk.StringVar(self, "")
        self.bgColorLabel = ttk.Label(self, text="Background: ", style="text.TLabel")
        self.bgColorLabel.grid(row=6, column=0, columnspan=2)
        self.bgColorButton = ttk.Button(self, text='Select a BackgroundColor', command=self.changeColor)
        self.bgColorButton.grid(row=6, column=1, columnspan=8, pady=20, padx=20)
        self.colorLabel = ttk.Label(self, text=".   PREVIEW   .", style="text.TLabel")
        self.colorLabel.grid(row=6, column=3, columnspan=2)

        self.fontLabel = ttk.Label(self, text="Font Family: ", style="text.TLabel")
        self.fontLabel.grid(row=7, column=0, columnspan=2)
        self.fonts = ["Arial", "Comic Sans MS", "Courier New", "Impact", "Georgia", "Lexend", "MS Gothic"]
        self.fontsCombobox = ttk.Combobox(self, values=self.fonts, font=("Arial", 12))
        self.fontsCombobox.grid(row=7, column=1, columnspan=8, pady=20, padx=20)

        self.submitButton = ttk.Button(self, text="Create my Website!", command=self.createWebsite)
        self.submitButton.grid(row=8, column=0, columnspan=10, padx=20, pady=20)
        self.errorLabel = ttk.Label(self, text="")
        self.errorLabel.grid(row=9, column=0, columnspan=10, pady=20, padx=20)

        button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame("Home"))
        button1.grid(row=10, column=3)

    # ~~~~~~~~~~~~ Form Functions ~~~~~~~~~~~~~~~
    # color picker
    def changeColor(self):
        colors = askcolor(title="Tkinter Color Chooser")
        # print(colors)
        self.colorLabel.configure(background=colors[1])
        self.bgColorVar = colors[1]
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Error Handling for Empty HTML Inputs
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # row 1 username and site title
    def checkName(self):
        userName = self.nameEntry.get()
        if userName == "":
            self.errorLabel.config(text="Error: Please Enter a Name.", foreground="red", font=("Arial", 14))
            return False
        else:
            return userName
        
    def checkSiteTitle(self):
        siteTitle = self.siteTitleEntry.get()
        if siteTitle == "":
            return "Personal Book Journal"
        else:
            return siteTitle
    # row 2 book title and author
    def checkBookTitle(self):
        bookTitle = self.bookTitleEntry.get()
        if bookTitle == "":
            self.errorLabel.config(text="Error: Please Enter a Book Title.", foreground="red", font=("Arial", 14))
            return False
        else:
            return bookTitle
    def checkAuthor(self):
        author = self.authorEntry.get()
        if author == "":
            return "Unknown"
        else:
            return author
    # row 3 date read and rating
    def checkDate(self):
        date = self.dateEntry.get()
        if date == "":
            return "Recently"
        else:
            return date
    def checkRating(self):
        rating = self.ratingEntry.get()
        if rating == "":
            return "OK Read"
        else:
            return rating
    # row 4 description and cover image
    def checkDesc(self):
        desc = self.descEntry.get("1.0", tk.END)
        if desc == "":
            return "It was okay, but not interesting enough for me to write a review."
        else:
            return desc
    def checkCover(self):
        img = self.imgEntry.get()
        if img == "":
            return "https://images.pexels.com/photos/6373305/pexels-photo-6373305.jpeg"
        else:
            return img
        
    def checkBGColor(self):
        bgColor = self.bgColorVar
        print(bgColor)
        if bgColor == "":
            return False
        else:
            return bgColor
    
    def checkFont(self):
        font = self.fontsCombobox.get()
        print(font)
        if font == "":
            return False
        else:
            return font

    # Call error handling functions and write files
    def createWebsite(self):
        # HTML Input Entries
        name = self.checkName()
        siteTitle = self.checkSiteTitle()
        bookTitle = self.checkBookTitle()
        author = self.checkAuthor()
        date = self.checkDate()
        rating = self.checkRating()
        desc = self.checkDesc()
        coverImg = self.checkCover()
        # CSS
        bgColor = self.checkBGColor()
        fontFamily = self.checkFont()

        if name and bookTitle:
            self.errorLabel.destroy()
            writeJSONfile(name, siteTitle, bookTitle, author, date, rating, desc, coverImg)
            writeHTMLFile(name, siteTitle, bookTitle, author, date, rating, desc, coverImg)
            writeCSSFile(bgColor, fontFamily)

    def readFile(self):
        with open('..\\server\\user.json', 'r') as f:
            data = json.load(f)
        return data