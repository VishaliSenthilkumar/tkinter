from tkinter import *

class ChangeLabel:
    def __init__(self):
        window = Tk()
        window.title("Change Label")

        frame1 = Frame(window)
        frame2 = Frame(window)
        frame1.pack()
        frame2.pack()

        self.lb1 = Label(frame1,text="Programming is fun")
        self.lb1.pack()

        lb2 = Label(frame2,text="Enter the message : ")

        self.msg=StringVar()
        entry = Entry(frame2, textvariable=self.msg)

        changelb = Button(frame2,text="Change label",command=self.change)

        self.val = StringVar()
        rbRed = Radiobutton(frame2,text="red",bg="red", variable = self.val, value='R' ,command=self.radio)
        rbBlue = Radiobutton(frame2,text="blue",bg="blue", variable = self.val, value='B' ,command=self.radio)

        lb2.grid(row=1, column=1)
        entry.grid(row=2,column=1)
        changelb.grid(row=3,column=1)
        rbRed.grid(row=3,column=2)
        rbBlue.grid(row=3,column=3)


        window.mainloop()

    def change(self):
        self.lb1["text"] = self.msg.get()

    def radio(self):
        if(self.val.get()=='R'):
            self.lb1["fg"] = "red"
        else:
            self.lb1["fg"] = "blue"

ChangeLabel()