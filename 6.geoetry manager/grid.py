# Tkinter uses a geometry manager to place widgets inside a container.

# Tkinter supports three geometry managers: 
    # the grid manager, 
    # the pack manager,  
    # the place manager

# The grid manager places widgets into the cells of an invisible grid in a container. 
# You can place a widget in a specified row and column. 
# You can also use the rowspan and columnspan parameters to place a widget in multiple rows and columns.

from tkinter import *

class GridManager:
    window = Tk()
    window.title("Grid Manager")

    message = Message(window,text="[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[occupies 3 rows and 3 columns]]]]]]]]]]]]]]]]]]]]]]]]]")
    message.grid(row=1,column=1,rowspan=3,columnspan=3)

    Label(window, text = "First Name:").grid(row = 2, column = 4)
    Entry(window).grid(row = 2, column = 5, rowspan=3, pady = 5)
    Label(window, text = "Last Name:").grid(row = 3, column = 4)
    Entry(window).grid(row = 2, column = 5)
    Button(window, text = "Get Name").grid(row = 4, padx = 5, pady = 5, column = 5, sticky=E )

    window.mainloop()

GridManager()



# The Get Name button uses the sticky = E to stick to the east in the cell so that it is right aligned with the Entry widgets in the same column.
# The sticky option defines how to expand the widget if the resulting cell is larger than the widget itself. 
# The sticky option can be any combination of the named constants S, N, E, and W, or NW, NE, SW, and SE.
# The padx and pady options pad the optional horizontal and vertical space in a cell. 
# You can also use the ipadx and ipady options to pad the optional horizontal and vertical space inside the widget borders.