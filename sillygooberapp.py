# Dum---s stupid f---ng modules:
from tkinter import *
from tkinter import ttk
import webbrowser

# Setting the root
root = Tk()

# Making rickrolls possible
def rickroll():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")

# Titling the app using hte room func
root.title("Goober Application")

# Setting up the "mainframe"
frm = ttk.Frame(root, padding=20)
frm.grid(row=0, column=0, pady=10, sticky="nsew")

# Setting up for the next entry (it's midnight and my brain hurts)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Trying to make things a lot easier (and less messy) but miserably failing and then replacing all the code
frm.columnconfigure(0, weight=1)
for i in range(3):
    frm.rowconfigure(i, weight=1)

# All the interactables
ttk.Label(frm, text="Hello World!").grid(column=0, row=0, pady=10, sticky="n")
ttk.Button(frm, text="EXPLODE", command=root.destroy).grid(column=0, row=1, pady=10)
ttk.Button(frm, text="Silly Goober Activities HERE", command=rickroll).grid(column=0, row=2, pady=10, sticky="nsew")

# root.mainloop makes it so that you can interact (and even see) everything on your window
root.mainloop()