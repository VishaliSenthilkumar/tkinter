# The pack manager can place widgets on top of each other or place them side by side. 
# You can also use the fill option to make a widget fill its entire container

# The fill option uses named constants X, Y, or BOTH to fill horizontally, vertically, or both ways. 
# The expand option tells the pack manager to assign additional space to the widget box. 
# If the parent widget is larger than necessary to hold all the packed widgets, any extra space is distributed among the widgets whose expand option is set to a nonzero value.

from tkinter import *

class PackManager:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager")

        Label(window, text="Blue", bg="blue").pack(side=LEFT)
        Label(window, text="Red", bg="red").pack(fill=BOTH, expand=1)
        Label(window, text="Yellow", bg="yellow").pack(fill=Y)

        window.mainloop()

PackManager()



# The side option can be LEFT, RIGHT, TOP, or BOTTOM.
# By default, it is set to TOP.