from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox
window = Tk()

mixer.init()

window.geometry('300x300')
window.title('Python Music Player')

def help_me():
    tkinter.messagebox.showinfo("Help", "How can I help you?")

def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar = Menu(window)
submenu = Menu(menubar,tearoff=0)
window.config(menu=menubar)

menubar.add_cascade(label="File",menu=submenu)
submenu.add_command(label="Open",command=browse_file)
submenu.add_command(label="Exit",command=window.destroy)
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="About Us",menu=submenu)
submenu.add_command(label="Help",command=help_me)



textLabel = Label(window,text="Music Player")
textLabel.pack()

def play_music():

    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing"
        except:
            tkinter.messagebox.showerror("File Error", "File Not Found")
    else:
        mixer.music.unpause()
        statusbar['text'] = "Resumed"

def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Stopped"

def set_volume(value):
    volume = int(value)/100
    mixer.music.set_volume(volume)

def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Paused"

def rewind_music():
    play_music()
    statusbar['text'] = "Rewinded"

frame = Frame(window)
frame.pack(padx=10,pady=10)

photo = PhotoImage(file='play2.png')
playButton = Button(frame,image=photo,command=play_music)
playButton.grid(row=0,column=0,padx=10)

stopphoto = PhotoImage(file='stop.png')
stopButton = Button(frame,image=stopphoto,command=stop_music)
stopButton.grid(row=0,column=1,padx=10)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(frame,image=pausePhoto,command=pause_music)
pauseBtn.grid(row=0,column=2,padx=10)

bottomframe = Frame(window)
bottomframe.pack()

rewindPhoto = PhotoImage(file='rewind.png')
rewindButton = Button(bottomframe,image=rewindPhoto,command=rewind_music)
rewindButton.grid(row=0,column=0)

scale = Scale(bottomframe,from_ =0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.grid(row=0,column=1)

statusbar = Label(window,text="Listening to music",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

window.mainloop()