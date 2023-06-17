# The Canvas widget for displaying shapes

# methods create_rectangle, create_oval, create_arc, create_polygon, or create_line to draw a rectangle, oval, arc, polygon, or line on a canvas.

from tkinter import *

class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canva")

        self.canvas = Canvas(window,width=200,height=100,bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        btRect = Button(frame,text="rectangle",command=self.disRect)
        btOval = Button(frame,text="oval",command=self.disOval)
        btArc = Button(frame,text="arc",command=self.disArc)
        btPolygon = Button(frame,text="polygon",command=self.disPolygon)
        btLine = Button(frame,text="line",command=self.disLine)
        btString = Button(frame,text="string",command=self.disString)
        btClear = Button(frame,text="clear",command=self.clear)

        btRect.grid(row = 1, column = 1)
        btOval.grid(row = 1, column = 2)
        btArc.grid(row = 1, column = 3)
        btPolygon.grid(row = 1, column = 4)
        btLine.grid(row = 1, column = 5)
        btString.grid(row = 1, column = 6)
        btClear.grid(row = 1, column = 7)

        window.mainloop()


    def disRect(self):
        self.canvas.create_rectangle(10,10,190,90,tags="rect")

    def disOval(self):
        self.canvas.create_oval(10,10,190,90,fill="red",tags="oval")

    def disArc(self):
        self.canvas.create_arc(10,10,190,90,tags="arc")

    def disPolygon(self):
        self.canvas.create_polygon(10,10,190,90,30,50,tags="polygon")

    def disLine(self):
        self.canvas.create_line(10,10,190,90,tags="line")

    def disString(self):
        self.canvas.create_text(100,50,text="HI, this is a canvas widget",font="Times 10 bold underline",tags="string")

    def clear(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

CanvasDemo()