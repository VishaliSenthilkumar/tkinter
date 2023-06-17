# A Tkinter widget can be bound to a function, which is called when an event occurs.
# Button widget is a good way to demonstrate the basics of event-driven programming

from tkinter import *

def ok():                        # callback function / handler
    print("Ok is clicked")

def cancel():
    print("Cancel is clicked")

window = Tk()

buttonOk = Button(window, text="ok", fg="red", command=ok)
buttonCancel = Button(window, text="cancel", bg="yellow", command=cancel)

buttonOk.pack()
buttonCancel.pack()

window.mainloop()