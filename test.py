import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")


root = tk.Tk()
root.title("Hello")

greet_but = ttk.Button(root, text = 'Greet', command = greet)
greet_but.pack(side= "left" , fill = 'x', expand = True)

quit_but = ttk.Button(root, text = 'Quit', command = root.destroy)
quit_but.pack(side= "left" , fill = 'x', expand = True)

###################################################################################################
# another code started

def greet1():
    print(f"Hello, {user_name.get() or 'world'}")

root = tk.Tk()
root.title("Greeter")
user_name = tk.StringVar()

name_label = ttk.Label(root, text = "Name: ")
name_label.pack(side= "left", padx= (0,10))
name_entry = ttk.Entry(root, width = 15, textvariable = user_name)
name_entry.pack(side = 'left', expand = True)
name_entry.focus()

greet_but = ttk.Button(root, text = 'Greet', command = greet1)
greet_but.pack(side= 'left', fill= 'x', expand= True)

root.mainloop()
##########################################################################################