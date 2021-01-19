import tkinter as tk
from tkinter import ttk

root = tk.Tk()
main = ttk.Frame(root)
main.pack(side='left', fill= 'both', expand= True)

tk.Label(main, text= 'Lebel', bg= 'green').pack(side= 'top', fill = 'both', expand = True)
tk.Label(main, text= 'Lebel', bg= 'green').pack(side= 'top', fill = 'both', expand = True)
tk.Label(root, text= 'Lebel', bg= 'red').pack(side= 'left' ,fill = 'y')

root.mainloop()