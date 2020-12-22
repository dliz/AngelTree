from tkinter import *

# root = blank window
# create and place text on screen
# grid lets you place text by row and column
# but is relative to each label
root = Tk()
theLabel = Label(root, text= "This is a test")
thelabel2 = Label(root, text= "Salvation Army")
theLabel.grid(row= 0, column= 0)
thelabel2.grid(row= 1, column= 0)

def myClick():
    thelabel1 = Label(root, text= "I clicked a button!")
    thelabel1.grid(row= 2, column =2)

# buttons
# padx/pady change size of button
# fg is text color, bg is background color
myButton = Button(root, text= "Click here!", command= myClick, fg= "blue", bg= "green")
myButton.grid(row= 2, column= 2, padx= 50, pady= 25)

# Entry is for typing into text box
namebox = Entry(root, width= 50)
namebox.grid(row = 1, column = 2)

# mainloop makes it so that the pop up screen stays open all the time till closed
# should be placed under entire code
# any code placed under will not appear on screen
root.mainloop()




print("Code for Angel Tree")
