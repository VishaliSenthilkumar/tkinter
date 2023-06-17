# Tkinter’s GUI classes define common GUI widgets such as buttons, labels, radio
# buttons, check buttons, entries, canvases, and others

from tkinter import * # Import all definitions from tkinter

class WidgetsDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Widgets Demo") # Set a title
        
        # Add a check button, and a radio button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack() 
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, command = self.check ) 
        
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red", value = 1, variable=self.v2, command = self.radio) 
        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", variable = self.v2, value = 2, command =self.radio ) 
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)

        # Add a label, an entry, a button, and a message to frame1
        frame2 = Frame(window) # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")

        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name ) 
        btGetName = Button(frame2, text = "Get Name", command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 2, column = 1)
        btGetName.grid(row = 3, column = 1)
        message.grid(row = 4, column = 1)
        
        # Add text
        text = Text(window) # Create and add text to the window
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")
        
        window.mainloop() # Create an event loop
        
    def check(self):
        print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))

    def radio(self): 
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected " )
    
    def processButton(self):
        print("Your name is " + self.name.get())
        
WidgetsDemo() # Create GUI



# Button             - A simple button, used to execute a command.
# Canvas             - Structured graphics, used to draw graphs and plots, create graphics editors, and implement custom widgets.
# Checkbutton        - Clicking a check button toggles between the values.
# Entry              - A text entry field, also called a text field or a text box.
# Frame              - A container widget for containing other widgets.
# Label              - Displays text or an image.
# Menu               - A menu pane, used to implement pull-down and popup menus.
# Menubutton         - A menu button, used to implement pull-down menus.
# Message            - Displays a text. Similar to the label widget, but can automatically wrap text to a given width or aspect ratio.
# Radiobutton        - Clicking a radio button sets the variable to that value, and clears all other radio buttons associated with the same variable.
# Text               - Formatted text display. Allows you to display and edit text with various styles and attributes. Also supports embedded images and windows