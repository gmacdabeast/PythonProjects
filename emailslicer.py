from tkinter import *
from tkinter import messagebox



def sliceEmail():
    print('good')
    email = tfirst.get()
    print(email)
    userName = email[:email.index('@')]
    domain = email[email.index('@') +1:]
    print(f"The userName is {userName} and the domain is {domain}")
    messagebox.showinfo('title',f"The userName is {userName} and domain is {domain}")

gui = Tk()
gui.title('Email Slicer')

#text entry areas
firstLabel = Label(gui, text= 'Email')
tfirst = Entry(gui, width =25,  highlightbackground= 'Blue')

#the button for the gu
x = Button(gui, text="Submit", command=sliceEmail)

firstLabel.pack()
tfirst.pack()
x.pack()
gui.mainloop()