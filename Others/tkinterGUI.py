# tkinter GUI (Graphical user interface)

# Mathod 1
# from tkinter import *
# gui = Tk()
# gui.geometry("300x400")
# gui.mainloop()


# Method 2
import tkinter as tk
window = tk.Tk()
window.geometry("600x600")
window.title('GUI Practice')
greeting = tk.Label(text="Hello, Tkinter").pack()
button = tk.Button(window, text='Stop', 
        width=25, 
        bg="blue", # Set the button color to blue
        fg="yellow", # Set the button text color to yellow
        command=window.destroy)
button.pack()


label = tk.Label(text="Goodbye, Tkinterers",
        foreground="white",  # Set the text color to white
        background="black",  # Set the background color to black
        width=15,
        height=5,
        ).pack()



label = tk.Label(text="Please insert your name below:").pack()
entry = tk.Entry()
entry.pack()
name = entry.get()



window.mainloop()

