from pytube import YouTube
from tkinter import *
from tkinter import messagebox

def downloadYoutube():

    #gui get()
    ytVideo = textBox.get()
    
    try:
        #Youtube object
        yt = YouTube(ytVideo)
        print(yt.title)

        video = yt.streams.first()

        video.download()

        messagebox.showinfo('we good', 'download successful!')

    except:
        messagebox.showerror('ERROR','LINK DOES NOT EXIST')

   # print(yt.title)

    #print confirmation
    print('downloaded')





#gui object
gui = Tk()
gui.title('Youtube Downloader')
#label and text area
label = Label(gui, text='Enter a Youtube link')
textBox = Entry(gui, width=25)
#button
button = Button(gui, text='Download Info', command=downloadYoutube)


label.pack()
textBox.pack()
button.pack()
gui.mainloop()