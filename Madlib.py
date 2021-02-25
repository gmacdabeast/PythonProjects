from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

#gui for madlibs
def madLibsForm():
    #define gui and parameters
    gui = Tk()
    gui.geometry("300x200")

    #the button for the gu
    x = Button(gui, text="enter", command=activateMadLibs)

    #run the gui
    x.pack()
    gui.mainloop()

#makesbuttondosomething
def activateMadLibs():  
    gatherMadLibInputs()

def gatherMadLibInputs():
    name1 = raw_input('Enter a name: ')
    adjective1 = raw_input('Enter an adjective: ')
    pronoun1 = raw_input('Enter a pronoun: ')
    adjective2 = raw_input('Enter an adjective: ')
    adjective3 = raw_input('Enter an adjective: ')
    adjective4 = raw_input('Enter an adjective: ')
    subject1 = raw_input('Enter an subject: ')
    adjective5 = raw_input('Enter an adjective: ')
    name2 = raw_input('Enter an name: ')

    #print the madlib results
    print(name1 + ' is the' + adjective1 + ' teacher in the world ' + pronoun1 + ' is ' + adjective2 +' and ' 
    + adjective3 + '. ' + name1 +' makes learning ' + adjective4 + ', especially in ' + subject1
    + '. School is ' + adjective5 + ' because of ' + pronoun1)
#main method
def main():
    madLibsForm()
    print('main successful')
if (__name__ == "__main__"):
    main()


