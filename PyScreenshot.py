# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO TAKE SCREENSHOT

# Importing necessary packages
import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

#---

# Defining CreateWidgets function to create the widgets
def CreateWidgets():
    labelattachmentEmail = Label(root, text="SAVE AS : ", font=('', 10, 'bold'),
                                 bg="darkslategrey")
    labelattachmentEmail.grid(row=1, column=0, pady=5, padx=5)

    root.entryattachmentEmail = Entry(root, width=30)
    root.entryattachmentEmail.grid(row=1, column=1, pady=5, padx=5)

    buttonattachmentEmail = Button(root, text="BROWSE", command=Browse, width=10)
    buttonattachmentEmail.grid(row=1, column=2, pady=5, padx=5)

    buttonattachmentEmail = Button(root, text="CAPTURE", command=Screenshot, width=10)
    buttonattachmentEmail.grid(row=2, column=1, pady=5, padx=5)

#---

# Defining Browse function to save the image
# Set initialdir to a path of your choice to save the screenshot
def Browse():
    root.fileName = filedialog.asksaveasfilename(title = "SAVE AS",
                                initialdir = "C:\Python\PySCREEN",
                                defaultextension = ".png",
                                filetypes = (("PNG Files","*.png"),("All Files","*.*")))
    root.entryattachmentEmail.insert('1', root.fileName)

# Defining Screenshot function to take screenshot
def Screenshot():
    # Taking the screenshot and saving in screenshot variable
    screenshot = pyautogui.screenshot()

    # Saving the screenshot variable in user-input location with user-input name
    screenshot.save(root.fileName)
    messagebox.showinfo("SUCCESS","SCREENSHOT CAPTURED")

#---

# Creating object root of tk
root = tk.Tk()

# Setting the title and background color
# disabling the resizing property
root.title("PySCREEN")
root.resizable(False,False)
root.config(background = "darkslategrey")

# Calling the CreateWidgets() function with argument bgColor
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
