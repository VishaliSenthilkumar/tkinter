# Tkinter enables you to develop GUI programs and is an excellent pedagogical tool for
# learning object-oriented programming.

from tkinter import *                        # import all definitions from tkinter

# The tkinter module contains the classes for creating GUIs. 
# The Tk class creates a window for holding GUI widgets (i.e., visual components).

root = Tk()                                   # create a window

# Label is a python tkinter widget class for creating labels.
# The first argument of a widget class is always the parent container (i.e., the container in which the widget will be placed). 

label = Label(root, text="Hello World")       # create the label
label.pack()                                  # place the label

root.mainloop()                               # create an event loop
