import random
import tkinter
from random import *
from tkinter import *
from tkinter import messagebox
def main():
    global result
    global number
    global listL
    global randomList


    createList()
    randomList.sort()

    number = numberEntry.get()
    convertNumber = int(number)
    listL = listEntry.get()
    convertList = int(listL)
    result = binarySearch(randomList, 0, len(randomList)-1, number)
    print(result)

    if result != -1:
        print('found')
    else:
        print('not found')


#create gui
gui = Tk()
gui.title('Binary Search Fun!!')

#label for created list
listLabel = Label(gui, text = 'Enter a size for the list:')
listEntry = Entry(gui, width = 25)

#Lable for number to search for
numberLabel = Label(gui, text ='Enter a number to search for:')
numberEntry = Entry(gui, width=25)

submitButton = Button(gui, text='Search Number' , command= main)

#Declare your list
randomList = []
number = None
listL = None
result = None











#List Creation
def createList():
    
    x = int(listEntry.get())
    
    for i in range (0,x):
        rand = randint(0,50)
        randomList.append(rand)
    
    #print(randomList)
    messagebox.showinfo('title', f'The list you created is: {randomList}')



#Search binary
def binarySearch(list, low, high, num):
    print(randomList)
    print(high)
    numConvert = int(num)
    mid = round((low+high)/2)
    #print(mid)
    #let's do the search
    if high>=low:
        if list[mid] == numConvert:
            return numConvert
        elif list[mid] < numConvert:
            return binarySearch(randomList, mid+1, high, number)
        elif list[mid] > numConvert:
            return binarySearch(randomList, low, mid-1, number )
    else:
        return -1









          






#Activate the Gui
listLabel.pack()
listEntry.pack()
numberLabel.pack()
numberEntry.pack()
submitButton.pack()
gui.mainloop()



