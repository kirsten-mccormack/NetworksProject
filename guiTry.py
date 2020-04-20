import tkinter as tk 
from tkinter import messagebox

window = tk.Tk() 

def welcomeWindow(): 
    messagebox.showinfo("Kickass FTP GUI", " Welcome to our project!")
#  Widgets go here apparently....

w = tk.Button ( window , text = ' Hey Friend!!' , bg = "red", command = welcomeWindow )
w.pack()

C = tk.Canvas(window, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()

window.mainloop()