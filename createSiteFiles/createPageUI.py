import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from writeHTML import *
from writeCSS import *

# Used https://customtkbuilder.com/

class CreatePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Your Own HTML Site!")
        self.root.geometry("700x700")
        self.root.configure(bg="#B8FFFA")
        # Styling
        style = ttk.Style()
        style.configure("title.TLabel", foreground="black", background="#B8FFFA", font=('Courier New', 18))
        style.configure("text.TLabel", foreground="black", background="#B8FFFA", font=('Arial', 14))
        style.configure("note.TLabel", foreground="#FF4255", background="#B8FFFA", font=('Arial', 12))
        style.configure("TEntry", foreground = "blue")

        # HTML Title
        self.greetLabel = ttk.Label(self.root, text="Hello! Let's create your very own HTML page!", style="title.TLabel")
        self.greetLabel.grid(row=0, column=0, columnspan=5, pady=20, padx=20)

        # User Inputs for HTML Page
        self.nameLabel = ttk.Label(self.root, text="Name: ", style="text.TLabel")
        self.nameLabel.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
        self.nameEntry = ttk.Entry(self.root, style="TEntry", width=50)
        self.nameEntry.grid(row=1, column=1, columnspan=3, pady=20, padx=20)

        self.hobbiesLabel = ttk.Label(self.root, text="Hobbies: ", style="text.TLabel")
        self.hobbiesLabel.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
        self.hobbiesEntry = ttk.Entry(self.root, style="TEntry", width=50)
        self.hobbiesEntry.grid(row=2, column=1, columnspan=3, pady=20, padx=20)

        self.hobbyNoteLabel = ttk.Label(self.root, text="*Note: Please separate each hobby with a comma. ", style="note.TLabel")
        self.hobbyNoteLabel.grid(row=3, column=0, columnspan=4, padx=20)

         # CSS Title
        self.greetLabel = ttk.Label(self.root, text="Time to Style Your Site! If you prefer, \nyou can use our default styling.", style="title.TLabel")
        self.greetLabel.grid(row=4, column=0, columnspan=5, pady=(75, 20), padx=20)
        # CSS Use Default
        self.agree = tk.BooleanVar(self.root, True)
        self.checkbox = ttk.Checkbutton(
            self.root,
            text='Use Default Styling - If checked, you can skip the next CSS inputs and default styling will be used.',
            command=self.checkCSSChoice,
            variable=self.agree
        )
        self.checkbox.grid(row=5, column=0, columnspan=5, pady=20, padx=20)

        # User Inputs for CSS
        self.bgColorVar = tk.StringVar(self.root, "")
        self.bgColorLabel = ttk.Label(self.root, text="Background: ", style="text.TLabel")
        self.bgColorLabel.grid(row=6, column=0, columnspan=2, pady=20, padx=20)
        self.bgColorButton = ttk.Button(self.root, text='Select a BackgroundColor', command=self.changeColor)
        self.bgColorButton.grid(row=6, column=1, columnspan=3, pady=20, padx=20)
        self.colorLabel = ttk.Label(self.root, text=".   color   .", style="text.TLabel")
        self.colorLabel.grid(row=6, column=3, columnspan=2, pady=20, padx=20)

        self.fontLabel = ttk.Label(self.root, text="Font Family: ", style="text.TLabel")
        self.fontLabel.grid(row=7, column=0, columnspan=2, pady=20, padx=20)
        self.fonts = ["Arial", "Comic Sans MS", "Courier New", "Impact", "Georgia", "Lexend", "MS Gothic"]
        self.fontsCombobox = ttk.Combobox(root, values=self.fonts, font=("Arial", 12))
        self.fontsCombobox.grid(row=7, column=1, columnspan=3, pady=20, padx=20)

        self.submitButton = ttk.Button(self.root, text="Create my Website!", command=self.createWebsite)
        self.submitButton.grid(row=8, column=0, columnspan=5, padx=20, pady=20)
        self.errorLabel = ttk.Label(self.root, text="")
        self.errorLabel.grid(row=9, column=0, columnspan=5, pady=20, padx=20)

    # ~~~~~~~~~~~~ Form Functions ~~~~~~~~~~~~~~~
    # color picker
    def changeColor(self):
        colors = askcolor(title="Tkinter Color Chooser")
        # print(colors)
        self.colorLabel.configure(background=colors[1])
        self.bgColorVar = colors[1]

    # default or user Styling
    def checkCSSChoice(self):
        # print(self.agree.get())
        if self.agree.get():
            print("Use Default Styling")
        else:
            print("User will input their CSS Choices")

    # Error Handling for Empty HTML Inputs
    def checkName(self):
        userName = self.nameEntry.get()
        if userName == "":
            self.errorLabel.config(text="Error: Please Enter a Name.", foreground="red", font=("Arial", 14))
            return False
        else:
            return userName
        
    def checkHobbies(self):
        hobbies = self.hobbiesEntry.get()
        if hobbies == "":
            self.errorLabel.config(text="Error: Please Enter your Hobbies.", foreground="red", font=("Arial", 14))
            return False
        else:
            return hobbies
        
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
        name = self.checkName()
        hobbies = self.checkHobbies()
        bgColor = self.checkBGColor()
        fontFamily = self.checkFont()

        if name and hobbies:
            self.errorLabel.destroy()
            writeHTMLFile(name, hobbies)
            writeCSSFile(bgColor, fontFamily)

    # ~~~~~~~~~~~~ Writing File Functions ~~~~~~~~~~~~~~~
    # ~~~~ See writeHTML.py file
    # ~~~~ See writeCSSL.py file

    def readFile():
        f = open('index.html')
        contents = f.read() # reads file text into string
        print(contents)
        f.close()