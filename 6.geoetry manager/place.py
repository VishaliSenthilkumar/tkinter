# The place manager places widgets in absolute positions.

from tkinter import *

class PlaceManager:
    def __init__(self):
        window = Tk()
        window.title("Place Manager")

        Label(window, text="Blue", bg="blue").place(x = 20, y = 20)
        Label(window, text="Red", bg="red").place(x = 50, y = 50)
        Label(window, text="Yellow", bg="yellow").place(x = 80, y = 80)

        window.mainloop()

PlaceManager()
