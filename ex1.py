from tkinter import *

class RectOval:
    def __init__(self):

        self.isDiagram = 0

        window = Tk()
        window.title("Rectangle Or Oval")

        frame1 = Frame(window)
        frame2 = Frame(window)

        frame1.pack()
        frame2.pack()

        self.canvas = Canvas(frame1,width=200,height=100)
        self.canvas.pack()

        self.diagram = StringVar()
        rectButton = Radiobutton(frame2,text="Rectangle",variable=self.diagram,value='R',command=self.rect)
        rectButton.grid(row=1,column=2)
        rectButton = Radiobutton(frame2,text="Oval",variable=self.diagram,value='O',command=self.oval)
        rectButton.grid(row=1,column=3)

        self.fillval = IntVar()
        rectButton = Checkbutton(frame2,text="Fill",variable=self.fillval,command=self.fillColor)
        rectButton.grid(row=1,column=4)

        window.mainloop()

    def rect(self):
        self.delete()
        if self.fillval.get() == 1:
            self.canvas.create_rectangle(10,10,190,90,fill="red",tags="rect")
        else:
            self.canvas.create_rectangle(10,10,190,90,tags="oval")

    def oval(self):
        self.delete()
        if self.fillval.get() == 1:
            self.canvas.create_oval(10,10,190,90,fill="red",tags="rect")
        else:
            self.canvas.create_oval(10,10,190,90,tags="oval")

    def fillColor(self):
        if self.diagram.get()=='R':
            self.rect()
        elif self.diagram.get()=='O':
            self.oval()

    def delete(self):
        self.canvas.delete("rect","oval")

RectOval()