from tkinter import *
from tkinter import messagebox
import sqlite3

def retrieveContacts():
    
    con = sqlite3.connect('python.db')

    cur = con.cursor()

    #try:

    #string declarations
    tf = tfirst.get()
    tl = tlast.get()

    #check for blanks
    if tf =='' or tl =='':
        messagebox.showerror('Error', 'Cannot leave blank!')
        return
    #check for alphas
    if(tf.isalpha() == False or tl.isalpha ==False):
        messagebox.showerror('Alert','Can\'t enter numbers for names. Alpha only.')
        return

    #try except for phone number
    try:
        tp = tphone.get()
        if tp == '':
            messagebox.showerror('Error', 'Cannot leave blank!')
            return
        tp = int(tp)
    except ValueError:
        messagebox.showerror('Error', 'Only Enter numbers for phone!')
        return
    if tp == '':
        messagebox.showerror('Error', 'Cannot leave blank!')
    

    #length check
    if len(str(tp)) == 10:
        cur.execute("SELECT * from contacts where phoneNumber = ? OR firstName = ? OR lastName = ?", (tp,tf,tl))
        msg = cur.fetchone()
        print(msg)
        if not msg:
            print('Does not exist.')
            messagebox.showerror('Title', 'Does not Exist')
        else:
            messagebox.showinfo('Title', 'Contact found!\n' + str(msg))
    else:
        messagebox.showerror('Error', 'Must input 10 NUMERIC digits for Phone Number! Try again')

    

def insertContacts():
    print('money')
    con = sqlite3.connect('python.db')

    cur = con.cursor()



    tf = tfirst.get()
    tl = tlast.get()

 #check for blanks
    if tf =='' or tl =='':
        messagebox.showerror('Error', 'Cannot leave blank!')
        return
    #check for alphas
    if(tf.isalpha() == False or tl.isalpha() == False):
        messagebox.showerror('Alert','Can\'t enter numbers for names. Alpha only.')
        return


    try:
        tp = tphone.get()
        if tp == '':
            messagebox.showerror('Error', 'Cannot leave blank!')
            return
        tp = int(tp)
    except ValueError:
        messagebox.showerror('Error', 'Only Enter numbers for phone!')
        return
    if tp == '':
        messagebox.showerror('Error', 'Cannot leave blank!')



    if len(str(tp)) == 10:
        cur.execute("INSERT INTO contacts VALUES (NULL,?,?,?)", (tf, tl, tp))
        con.commit()
        cur.close()
        messagebox.showinfo('Title', 'Insertion Successful!')
    else:
        messagebox.showerror('Error', 'Must input 10 NUMERIC digits for Phone Number! Try again')



def deleteContacts():
    print('whatever')
    con = sqlite3.connect('python.db')

    cur = con.cursor()

    try:
        tp = tphone.get()
        if tp == '':
            messagebox.showerror('Error', 'Cannot leave blank!')
            return
        tp = int(tp)
    except ValueError:
        messagebox.showerror('Error', 'Only Enter numbers for phone!')
        return
    if tp == '':
        messagebox.showerror('Error', 'Cannot leave blank!')

    

    if len(str(tp)) == 10:
        cur.execute('SELECT * From contacts where phoneNumber = ?', (tp,))
        if cur.fetchone():
            cur.execute('DELETE from contacts WHERE phoneNumber = ?', (tp,))
            con.commit()
            cur.close()
            messagebox.showinfo('Title', 'Deletion Successful!')
        else:
            messagebox.showerror('Error','Record doesn\'t exist.')
            return
    else:
        messagebox.showerror('Error', 'Must input 10 NUMERIC digits for Phone Number! Try again')
    


    

#define gui and parameters
gui = Tk()
gui.geometry("300x300")
gui.title('THE CONTACTS APP!')


#text entry areas
firstLabel = Label(gui, text= 'FirstName')
tfirst = Entry(gui, width =25,  highlightbackground= 'Blue')
lastLabel = Label(gui, text= 'LastName')
tlast = Entry(gui, width = 25, highlightbackground= 'Green')
phoneLabel = Label(gui, text = 'Phone Number')
tphone = Entry(gui, width = 25, highlightbackground= 'Black')

#the button for the gu
x = Button(gui, text="Retrieve", command=retrieveContacts)
#x.grid(column=2, row = 20)

y = Button(gui, text ="Insert", command=insertContacts)
#y.grid(column=4, row = 20)

z = Button(gui, text = "Delete", command=deleteContacts)
#z.grid(column=6 , row =20)


#run the gui
firstLabel.pack()
tfirst.pack()
lastLabel.pack()
tlast.pack()
phoneLabel.pack()
tphone.pack()
x.pack(side = BOTTOM)
y.pack(side = BOTTOM)   
z.pack(side = BOTTOM)
gui.mainloop()
print('gui successful')


