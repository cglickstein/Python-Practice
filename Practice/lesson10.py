from tkinter import *
from tkinter import ttk
#you have this environment and everything based off of activities of the user. event driven user- order doesn't matter, whatever user presses it responds to

root = Tk() #root is the base off of what your program is. invokes the tkinter environment
#replaced when we build upon it

#create a title for the window
root.title("WITS PROGRAM")

#sizing
root.geometry("300x200")

#add a frame to the root to put all of your widgets on
frm=ttk.Frame(root, padding=10) #gonna be in the root

#layout arrange widgets
frm.grid() #method for widgets that affects layout

#creat label within the frame
ttk.Label(frm,text="Welcome to the program!").grid(column=0, row=0)

#create a button within the frame
btnQuit= Button(frm,text="Quit")
btnQuit.grid()
#command means when you click what's it gonna do
btnQuit2= Button(frm,text="Quit- works",command=root.destroy).grid(column=1,row=0)
#method that kicks off the event loop 

#change button text. configure means your changing something
btnQuit.configure(text="This button doesn't do anything")

#buttons are event driven so doesn't wait for the code




root.mainloop()


